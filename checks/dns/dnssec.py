#! /usr/bin/env python3

import os
import sys
import json
from shlex import quote

dnsResolver = "8.8.8.8"

def main():
    """Main function
    """
    target = sys.argv[1]

    testdnssec(target)

def testdnssec(domain):
    """Test if DNSSEC is enabled for a specific domain.

    Args:
        domain (str): Input options.
    """

    dig_requests = os.popen('dig @%s %s +noall +comments +dnssec'%(dnsResolver, quote(domain))).read()

    # Check ad flag
    if "ad;" in dig_requests:
        ad_flag = 1
    else:
        ad_flag = 0

    # Check SERVFAIL flag
    if "SERVFAIL," in dig_requests:
        status_error = 1
    else:
        status_error = 0

    # Check NOERROR flag
    if "NOERROR," in dig_requests:
        status_noerror = 1
    else:
        status_noerror = 0

    if ad_flag == 1 and status_noerror == 1:
        print(json.dumps({
            "name": "DNSSEC",
            "score": 10,
            "message": "Domain %s is safe, it uses a valid DNSSEC.",
            "description": "DNSSEC"
        }) % domain)
    elif status_error == 1:
        print(json.dumps({
            "name": "DNSSEC",
            "score": 5,
            "message": "Domain %s uses DNSSEC but is misconfigured or invalid.",
            "description": "DNSSEC"
        }) % domain)

    elif status_noerror == 1 and ad_flag == 0:
        print(json.dumps({
            "name": "DNSSEC",
            "score": 0,
            "message": "Domain %s does not use DNSSEC.",
            "description": "DNSSEC"
        }) % domain)
    else:
        print(json.dumps({
            "name": "DNSSEC",
            "score": 0,
            "message": "Cannot read the result.",
            "description": "DNSSEC"
        }) % domain)

if __name__ == '__main__':
    main()
