import socket, sys, ssl


DOMAIN = sys.argv[1]
context = ssl.create_unverified_context()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslSocket = context.wrap_socket(s, server_hostname = DOMAIN)

try:
    sslSocket.connect((DOMAIN, 443))
except:
    print("Dit domein bestaat niet")
    sslSocket.close()

else:
    versie = sslSocket.version()
    if "TLSv1.2" in versie or "TLSv1.3" in versie:
        print(f'{{"name": "protocol", "score": 10, "message": "Uw domein {DOMAIN} heeft versie {versie}."}}')
    else:
        print(f'{{"name": "protocol", "score": 0, "message": "Uw domein {DOMAIN} heeft versie {versie}." }}')
    sslSocket.close()
