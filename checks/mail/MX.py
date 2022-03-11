#!/usr/bin/python3
import argparse
from asyncio.windows_events import NULL
import dns.resolver
import json
import os

parser = argparse.ArgumentParser(description='Simple MX quick test.')
parser.add_argument('domain', help='Domain name to test')
args = parser.parse_args()
domain = args.domain

def MXtest(domain):
    try:
        for x in dns.resolver.resolve(domain, 'MX'):
            check=x.to_text()
            if(check!=NULL):
                res={
                    "output":{"MX":"TRUE"}
                    }
            return res                
    except:
        res={}
    return res

response=MXtest(domain) 
jsonresult=json.dumps(response)
os.environ["MXresult"]=jsonresult
print (os.environ.get("MXresult"))