#!/usr/bin/python3
import argparse
import dns.resolver
import json
import os

def main(domain: str):
    """main.

    Args:
        domain (str): domain
    """
    if os.environ.get("MX") is None:
        print("{}")
        return

    print(json.dumps(spfTest(domain)))

def spfTest(domain):
    """Test if a SPF record is found for a specific domain.

    Returns:
        dict: A result object.
    """
    try:
        test_spf = dns.resolver.resolve(domain , 'TXT')
        for dns_data in test_spf:

            if 'spf1' in str(dns_data):
                result = {"name": "Mail: SPF", "score": 10, "message": "SPF record found."}
                return result

    except:
        result = {"name": "Mail: SPF", "score": 0, "message": "No SPF record found."}
        return result

if __name__ == "__main__":
    main(sys.argv[1])
