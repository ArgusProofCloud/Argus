from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


sleep(5)

options = Options()
options.add_argument("--incognito")
driver = webdriver.Remote('http://selenium:4444/wd/hub', DesiredCapabilities.CHROME)

DOMAIN = "spotify.com"
url = 'http://' + DOMAIN

driver.get(url)
cookies = driver.get_cookies()
domeinen = []
namen = []

for array in cookies:
    namen.append(array.get("name"))
    domeinen.append(array.get("domain"))
print(namen)
print(domeinen)

for domein in domeinen:
    if not DOMAIN in domein:
        print('{{"name": "cookie", "score": 0, "message": "Uw website %s maakt gebruik van third party cookies %s.}}' % (url, domein))
        exit()
print('{{"name": "cookie", "score": 10, "message": "Uw website %s maakt GEEN gebruik van third party cookies.}}' % (url))
