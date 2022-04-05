# SSL/TLS Certificates

## Why do I need a SSL/TLS Certificate?

TLS/SSL certificates are used to protect both the end users' information while it's in transfer, and to authenticate the website's organization identity to ensure users are interacting with legitimate website owners.

### Encryption

SSL/TLS Certificates provide end-to-end-encryption with the TLS or the discontinued and
unsafe SSL protocol. In short this means that a server and an end-user can
communicate with eachother without anyone else knowing what they are
communicating to eachother.

In short a bad actor cannot understand any of the communication between your
servers and your clients.

## How do I make a valid certificate?
For an SSL certificate to be valid, domains need to obtain it from a certificate authority (CA). A CA is an outside organization, a trusted third party, that generates and gives out SSL certificates. The CA will also digitally sign the certificate with their own private key, allowing client devices to verify it.

## Sources

[Source 1](https://www.digicert.com/how-tls-ssl-certificates-work#:~:text=TLS%2FSSL%20certificates%20are%20used,interacting%20with%20legitimate%20website%20owners.)

[Source 2](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/#:~:text=For%20an%20SSL%20certificate%20to,client%20devices%20to%20verify%20it.)
