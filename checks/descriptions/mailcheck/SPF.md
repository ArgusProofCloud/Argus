# Mailchecks (eng)
## Tests

### SPF
Sender Policy Framework (SPF) is an email authentication method designed to detect forging sender addresses during the delivery of the email. SPF alone, though, is limited to detecting a forged sender claim in the envelope of the email, which is used when the mail gets bounced. Only in combination with DMARC can it be used to detect the forging of the visible sender in emails (email spoofing), a technique often used in phishing and email spam.

SPF allows the receiving mail server to check during mail delivery that a mail claiming to come from a specific domain is submitted by an IP address authorized by that domain's administrators. The list of authorized sending hosts and IP addresses for a domain is published in the DNS records for that domain.



## Source
[link text SPF:](https://en.wikipedia.org/wiki/Sender_Policy_Framework)
[link SPF test:](https://github.com/juerkkil/securityheaders/blob/master/securityheaders.py)


# Mailchecks (nl)
## Testen

### SPF
Sender Policy Framework (SPF) is een e-mailverificatiemethode die is ontworpen om vervalste afzenderadressen te detecteren tijdens de bezorging van de e-mail. SPF alleen is echter beperkt tot het detecteren van een vervalste afzenderclaim in de envelop van de e-mail, die wordt gebruikt wanneer de e-mail wordt teruggestuurd. Alleen in combinatie met DMARC kan het worden gebruikt om vervalsing van de zichtbare afzender in e-mails te detecteren (email spoofing), een techniek die vaak wordt gebruikt bij phishing en e-mailspam.

Met SPF kan de ontvangende e-mailserver tijdens de e-mailbezorging controleren of een e-mail die beweert van een specifiek domein te komen, is ingediend door een IP-adres dat is geautoriseerd door de beheerders van dat domein. De lijst met geautoriseerde verzendende hosts en IP-adressen voor een domein wordt gepubliceerd in de DNS-records voor dat domein.

## Bron
[link tekst SPF:](https://en.wikipedia.org/wiki/Sender_Policy_Framework)
[link SPF test:](https://github.com/juerkkil/securityheaders/blob/master/securityheaders.py)