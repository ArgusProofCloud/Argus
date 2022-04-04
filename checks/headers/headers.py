#!/usr/bin/env python3

import re
import sys
import json
import requests

def main(domain: str):
    """main.

    Args:
        domain (str): domain
    """
    headerPatterns = loadPatterns()
    headers = getHeaders("https://" + domain)

    print(json.dumps(checkHeaders(headers, headerPatterns)))

def loadPatterns() -> dict:
    """Load header patterns from file.

    Returns:
        dict: A dictionary with all header patterns.
    """
    with open("./headers.json") as jsonFile:
        return json.load(jsonFile)

def getHeaders(url: str):
    """Get the headers from a web request.

    Args:
        url (str): The url to download from.
    """
    return requests.get(url, allow_redirects=True).headers

def checkHeaders(headers: dict, patterns: dict) -> list:
    """Check the headers against a header pattern.

    Args:
        headers (dict): Header map
        patterns (dict): Pattern map

    Returns:
        list: A list of results.
    """
    results = []

    for headerKey in patterns:
        pattern = patterns[headerKey]

        if headerKey not in headers and pattern["present"] is True:
            results.append({
                "name": headerKey,
                "score": 0,
                "message": f"{headerKey} should be present."
            })
        elif headerKey in headers:

            valueTest = False
            for value in pattern['values']:
                if len(re.findall(value['pattern'], headers[headerKey].lower())) > 0:
                    results.append({
                        "name": headerKey,
                        "score": value['score'],
                        "value": headers[headerKey]
                    })
                    valueTest = True
                    break

            if pattern['present'] is False and not valueTest:
                results.append({
                    "name": headerKey,
                    "score": 0,
                    "message": f"{headerKey} shoud be absent.",
                    "value": headers[headerKey]
                })
            elif not valueTest and pattern['present'] is None:
                results.append({
                    "name": headerKey,
                    "score": 10,
                    "value": headers[headerKey]
                })
            elif not valueTest:
                results.append({
                    "name": headerKey,
                    "score": 0,
                    "message": f"{headerKey} is not correctly configured.",
                    "value": headers[headerKey]
                })

        elif headerKey not in headers and pattern["present"] is False:
            results.append({
                "name": headerKey,
                "score": 10,
                "message": f"{headerKey} is correctly configured."
            })
        elif pattern['present'] is None:
            results.append({
                "name": headerKey,
                "score": 10
            })

    return results

if __name__ == "__main__":
    main(sys.argv[1])
