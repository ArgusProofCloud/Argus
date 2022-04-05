# Protocol

## SSL vs TLS

Secure Socket Layer (SSL) was the original protocol that was used to provide encryption for HTTP traffic, in the form of HTTPS. There were two publicly released versions of SSL - versions 2 and 3. Both of these have serious cryptographic weaknesses and should no longer be used.

For various reasons the next version of the protocol (effectively SSL 3.1) was named Transport Layer Security (TLS) version 1.0. Subsequently TLS versions 1.1, 1.2 and 1.3 have been released.

## Only Support Strong Protocols

The SSL protocols have a large number of weaknesses, and should not be used in any circumstances. General purpose web applications should default to TLS 1.3 (support TLS 1.2 if necessary) with all other protocols disabled.

## Sources

[Source 1](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
