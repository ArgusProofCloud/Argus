#! /usr/bin/env python3

from urllib import request
import sys

DOMAIN = sys.argv[1]
url = 'http://' + DOMAIN
HTTPS = "https"


try:
    response = request.urlopen(url)
except:
    try:
        url = 'http://www.' + DOMAIN
        response = request.urlopen(url)
    except:
        print("Dit domein bestaat niet.", file=sys.stderr)
        sys.exit()

new_url = response.geturl()
if HTTPS in new_url:
    print(f'{{"name": "redirect", "score": 10, "message": Alle potentieel onveilige verkeer via {url}, wordt veilig doorgestuurd naar {new_url}"}}')
else:
    print(f'{{"name": "redirect", "score": 0, "message": "Uw website {url} is bereikbaar via het onbeveiligde http, dit betekent dat in bepaalde gevallen bezoekers onversleuteld gegevens naar uw website kunnen doorsturen. Misschien kan u een redirectie naar https opzetten?"}}')
