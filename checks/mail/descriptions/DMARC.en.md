# Mailchecks (eng)
## Tests

### DMARC
DMARC (Domain-based Message Authentication, Reporting and Conformance) is an email authentication protocol. It is designed to give email domain owners the ability to protect their domain from unauthorized use, commonly known as email spoofing. The purpose and primary outcome of implementing DMARC is to protect a domain from being used in business email compromise attacks, phishing email, email scams and other cyber threat activities.

Once the DMARC DNS entry is published, any receiving email server can authenticate the incoming email based on the instructions published by the domain owner within the DNS entry. If the email passes the authentication, it will be delivered and can be trusted. If the email fails the check, depending on the instructions held within the DMARC record the email could be delivered, quarantined or rejected.

## Source
[link DMARC test:](https://github.com/juerkkil/securityheaders/blob/master/securityheaders.py)
[link text DMARC:](https://en.wikipedia.org/wiki/DMARC)

# Mailchecks (nl)
## Testen

### DMARC
DMARC (Domain-based Message Authentication, Reporting and Conformance) is een protocol voor e-mailverificatie. Het is ontworpen om eigenaren van e-maildomeinen de mogelijkheid te bieden hun domein te beschermen tegen ongeoorloofd gebruik, ook wel e-mailspoofing genoemd. Het doel en het primaire resultaat van de implementatie van DMARC is om een ​​domein te beschermen tegen gebruik in zakelijke e-mailaanvallen, phishing-e-mail, e-mailzwendel en andere cyberbedreigingsactiviteiten.

Zodra het DMARC DNS-item is gepubliceerd, kan elke ontvangende e-mailserver de inkomende e-mail verifiëren op basis van de instructies die door de domeineigenaar zijn gepubliceerd in het DNS-item. Als de e-mail de authenticatie doorstaat, wordt deze afgeleverd en kan deze worden vertrouwd. Als de e-mail niet door de controle komt, kan de e-mail, afhankelijk van de instructies in het DMARC-record, worden afgeleverd, in quarantaine worden geplaatst of worden afgewezen.

## Bron
[link tekst DMARC:](https://en.wikipedia.org/wiki/DMARC)
[link DMARC test:](https://github.com/juerkkil/securityheaders/blob/master/securityheaders.py)