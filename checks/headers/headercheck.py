#!/usr/bin/env python3

import http.client
import argparse
import socket
import ssl
import sys
import re
from urllib.parse import urlparse
import json

#var
score=0

class SecurityHeaders():
    """class SecurityHeaders
    """
    def __init__(self):
        pass

    def evaluateWarn(self, header, contents):
        """ Risk evaluation function.
        Set header warning flag (1/0) according to its contents.
        Args:
            header (str): HTTP header name in lower-case
            contents (str): Header contents (value)
        """
        warn = 1

        if header == 'x-frame-options':
            if contents.lower() in ['deny', 'sameorigin']:
                warn = 0
            else:
                warn = 1

        if header == 'strict-transport-security':
            warn = 0

        if header == 'content-security-policy':
            warn = 0

        if header == 'access-control-allow-origin':
            if contents == '*':
                warn = 1
            else:
                warn = 0

        if header.lower() == 'x-xss-protection':
            if contents.lower() in ['1', '1; mode=block']:
                warn = 0
            else:
                warn = 1

        if header == 'x-content-type-options':
            if contents.lower() == 'nosniff':
                warn = 0
            else:
                warn =1

        if header == 'x-powered-by' or header == 'server':
            if len(contents) > 1:
                warn = 1
            else:
                warn = 0

        return {'defined': True, 'warn': warn, 'contents': contents}

    def testHttps(self, url):
        """_summary_

        Args:
            self(security headers)
            url (string): url of the target

        Returns:
            json: result of the test
        """
        parsed = urlparse(url)
        protocol = parsed[0]
        hostname = parsed[1]
        path = parsed[2]
        sslerror = False

        conn = http.client.HTTPSConnection(hostname, context = ssl.create_default_context() )
        try:
            conn.request('GET', '/')
            res = conn.getresponse()
        except socket.gaierror:
            return {'supported': False, 'certvalid': False}
        except ssl.CertificateError:
            return {'supported': True, 'certvalid': False}
        except:
            sslerror = True

        # if tls connection fails for unexcepted error, retry without verifying cert
        if sslerror:
            conn = http.client.HTTPSConnection(hostname, timeout=5, context = ssl._create_stdlib_context() )
            try:
                conn.request('GET', '/')
                res = conn.getresponse()
                return {'supported': True, 'certvalid': False}
            except:
                return {'supported': False, 'certvalid': False}

        return {'supported': True, 'certvalid': True}

    def testHttpToHttps(self, url, followRedirects = 5):
        """try to redirect http to https

        Args:
            url (string): _description_

        Returns:
            boolean: _description_
        """
        parsed = urlparse(url)
        protocol = parsed[0]
        hostname = parsed[1]
        path = parsed[2]
        if not protocol:
            protocol = 'http' # default to http if protocl scheme not specified

        if protocol == 'https' and followRedirects != 5:
            return True
        elif protocol == 'https' and followRedirects == 5:
            protocol = 'http'

        if protocol == 'http':
            conn = http.client.HTTPConnection(hostname)
        try:
            conn.request('HEAD', path)
            res = conn.getresponse()
            headers = res.getheaders()
        except socket.gaierror:
            #if https request failed
            return False


        if (res.status >= 300 and res.status < 400  and followRedirects > 0):
            for header in headers:
                if header[0].lower() == 'location':
                    return self.testHttpToHttps(header[1], followRedirects - 1)

        return False

    def checkHeaders(self, url, followRedirects = 0):
        """ Make the HTTP request and check if any of the pre-defined
        headers exists.
        Args:
            url (str): Target URL in format: scheme://hostname/path/to/file
            followRedirects (Optional[str]): How deep we follow the redirects,
            value 0 disables redirects.
        """


        retval = {
            'x-frame-options': {'defined': False, 'warn': 1, 'contents': '' },
            'strict-transport-security': {'defined': False, 'warn': 1, 'contents': ''},
            'access-control-allow-origin': {'defined': False, 'warn': 0, 'contents': ''},
            'content-security-policy': {'defined': False, 'warn': 1, 'contents': ''},
            'x-xss-protection': {'defined': False, 'warn': 1, 'contents': ''},
            'x-content-type-options': {'defined': False, 'warn': 1, 'contents': ''},
            'x-powered-by': {'defined': False, 'warn': 0, 'contents': ''},
            'server': {'defined': False, 'warn': 0, 'contents': ''}
        }

        parsed = urlparse(url)
        protocol = parsed[0]
        hostname = parsed[1]
        path = parsed[2]
        if protocol == 'http':
            conn = http.client.HTTPConnection(hostname)
        elif protocol == 'https':

            ctx = ssl._create_stdlib_context()
            conn = http.client.HTTPSConnection(hostname, context = ctx )
        else:
            return {}

        try:
            conn.request('HEAD', path)
            res = conn.getresponse()
            headers = res.getheaders()

        except socket.gaierror:
            #if https request failed
            return False

        if (res.status >= 300 and res.status < 400  and followRedirects > 0):
            for header in headers:
                if header[0].lower() == 'location':
                    redirect_url = header[1]
                    if not re.match('^https?://', redirect_url):
                        redirect_url = protocol + '://' + hostname + redirect_url
                    return self.checkHeaders(redirect_url, followRedirects - 1)

        for header in headers:

            #set to lowercase before the check
            headerAct = header[0].lower()

            if headerAct in retval:
                retval[headerAct] = self.evaluateWarn(headerAct, header[1])

        return retval

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Check HTTP security headers', \
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('domain', metavar='domain', type=str, help='Target domain')
    args = parser.parse_args()
    domain=args.domain
    url = "https://"+domain
    redirects = 2

    foo = SecurityHeaders()

    parsed = urlparse(url)
    if not parsed.scheme:
        url = 'http://' + url # default to http if scheme not provided

    result=[]
    headers = foo.checkHeaders(url, redirects)

    if not headers:
        # if header is not correct
        sys.exit(1)

    for header, value in headers.items():
        #headers check
        if value['warn'] == 1:
            if value['defined'] is False:
                result.append({'name':header,"score":0,'message': header+" is missing"})
            else:
                result.append({'name':header,"score":0,'message': header+" contains value "+value['contents']})
        elif value['warn'] == 0:
            if value['defined'] is False:
                result.append({'name':header,"score":10,'message': header+" is missing"})
            else:
                result.append({'name':header,"score":10,'message': header+" contains value "+value['contents']})

    https = foo.testHttps(url)
    #check https check
    if https['supported']:
        result.append({'name':"Https","score":10,'message':"Https is supported"})

    else:
        result.append({'name':"Https","score":0,'message':"Https is not supported"})

    if https['certvalid']:
        result.append({'name':"Https certificate","score":10,'message':"Https cetificate is valid"})
    else:
        result.append({'name':"Https certificate","score":0,'message':"Https cetificate is not valid"})
    if foo.testHttpToHttps(url, 5):
        result.append({'name':"Http to Https","score":10,'message':"Can redirect from Http to Https"})
    else:
        result.append({'name':"Http to Https","score":0,'message':"Can not redirect from Http to Https"})

jsonresult = json.dumps(result)
print(jsonresult)
