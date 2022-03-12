#!/usr/bin/python3
import argparse
import dns.resolver
import json
import os

parser = argparse.ArgumentParser(description='Simple SPF quick test.')
parser.add_argument('domain', help='Domain name to test')
args = parser.parse_args()
domain = args.domain

def spefTest(domain):
    """Test if a SPF record is found for a specific domain.

    Returns:
        dict: A result object.
    """
    try:
        test_spf = dns.resolver.resolve(domain , 'TXT')
        for dns_data in test_spf:
            if 'spf1' in str(dns_data):
                mes = "[PASS] SPF record found."
                score = 10
                result = {"name": "SPF check", "score": score, "message": mes}
                return result
    except:
        mes = "[FAIL] SPF record not found."
        score = 0
        result = {"name": "SPF check", "score": score, "message": mes}
        return result

envvar = os.environ.get("MX")
if envvar != None:
    result = spefTest(domain)
    jsonresult = json.dumps(result)
else:
    jsonresult = {}
print(jsonresult)