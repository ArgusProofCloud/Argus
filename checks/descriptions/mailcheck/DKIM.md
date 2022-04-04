# Mailchecks (eng)
## Tests

### DKIM
DomainKeys Identified Mail(DKIM) is an email authentication method designed to detect forged sender addresses in email, a technique often used in phishing and email spam.

DKIM allows the receiver to check that an email claimed to have come from a specific domain was indeed authorized by the owner of that domain. It achieves this by affixing a digital signature, linked to a domain name, to each outgoing email message. The recipient system can verify this by looking up the sender's public key published in the DNS. A valid signature also guarantees that some parts of the email (possibly including attachments) have not been modified since the signature was affixed. Usually, DKIM signatures are not visible to end-users, and are affixed or verified by the infrastructure rather than the message's authors and recipients.

#### How to fix if DKIM record not presend
**Before you set up DKIM**
<ol>
  <li>Get the sign-in information for your domain provider</li>
  <li>Find out if your domain provider supports 2048-bit DKIM keys</li>
  <li>Check outbound gateway settings</li>
  <li>(Optional) Check for an existing DKIM key for your domain</li>
</ol>

**Turn on DKIM for your domain**
<ol>
  <li>Get your DKIM key in your Admin console</li>
  <li>Add your DKIM key at your domain provider</li>
  <li>Turn on DKIM in your Admin console</li>
  <li>Verify DKIM signing is on</li>
</ol>

**Troubleshoot DKIM issues**
<ol>
  <li>Verify DKIM is set up correctly</li>
  <li>Verify messages pass DKIM authentication</li>
  <li>Check message forwarding</li>
  <li>Contact your admin for servers that reject DKIM-authenticated messages</li>
  <li>Verify your domain providers TXT record character limits</li>
</ol>

## Source
[link text DKIM:](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail)
[link DKIM test:](https://github.com/juerkkil/securityheaders/blob/master/securityheaders.py)


# Mailchecks (nl)
## Testen

### DKIM
DomainKeys Identified Mail (DKIM) is een e-mailverificatiemethode die is ontworpen om vervalste afzenderadressen in e-mail te detecteren, een techniek die vaak wordt gebruikt bij phishing en e-mailspam.

Met DKIM kan de ontvanger controleren of een e-mail waarvan wordt beweerd dat deze afkomstig is van een specifiek domein, inderdaad is geautoriseerd door de eigenaar van dat domein. Dit doet zij door op elk uitgaand e-mailbericht een digitale handtekening te plaatsen, gekoppeld aan een domeinnaam. Het ontvangende systeem kan dit verifiëren door de openbare sleutel van de afzender op te zoeken die in de DNS is gepubliceerd. Een geldige handtekening garandeert ook dat sommige delen van de e-mail (eventueel inclusief bijlagen) niet zijn gewijzigd sinds de handtekening is aangebracht. Gewoonlijk zijn DKIM-handtekeningen niet zichtbaar voor eindgebruikers en worden ze aangebracht of geverifieerd door de infrastructuur in plaats van door de auteurs en ontvangers van het bericht.

#### Hoe op te lossen als DKIM-record niet aanwezig is?
**Voordat u DKIM instelt**
<ol>
  <li>De aanmeldingsgegevens voor uw domeinprovider ophalen</li>
  <li>Ontdek of uw domeinprovider 2048-bits DKIM-sleutels ondersteunt</li>
  <li>Instellingen van uitgaande gateway controleren</li>
  <li>(Optioneel) Controleer op een bestaande DKIM-sleutel voor uw domein</li>
</ol>

**Schakel DKIM in voor uw domein**
<ol>
  <li>Haal uw DKIM-sleutel op in uw beheerdersconsole</li>
  <li>Voeg uw DKIM-sleutel toe bij uw domeinprovider</li>
  <li>Schakel DKIM in uw beheerdersconsole in</li>
  <li>Controleer of DKIM-ondertekening is ingeschakeld</li>
</ol>

**DKIM-problemen oplossen**
<ol>
  <li>Controleer of DKIM correct is ingesteld</li>
  <li>Controleer of berichten DKIM-authenticatie passeren</li>
  <li>Controleer het doorsturen van berichten</li>
  <li>Neem contact op met uw beheerder voor servers die DKIM-geverifieerde berichten weigeren</li>
  <li>Controleer de tekenlimieten voor TXT-records van uw domeinproviders</li>
</ol>

## Bron
[link tekst DKIM:](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail)
[link DKIM test:](https://github.com/juerkkil/securityheaders/blob/master/securityheaders.py)