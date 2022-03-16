import socket
import ssl


context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False
context.options = ssl.OP_ALL


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(s, server_hostname='electronix.ru')
ssl_sock.connect(('electronix.ru', 443))

print(ssl_sock.version())
print(ssl_sock.cipher())
print(context.minimum_version)

# https://pythontic.com/ssl/sslcontext/sslcontext
# https://docs.python.org/3/library/ssl.html