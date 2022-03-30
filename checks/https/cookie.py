from selenium import webdriver
import sys

driver = webdriver.Firefox(executable_path="")

DOMAIN = sys.argv[1]
url = 'http://' + DOMAIN

driver.get(url)
cookies = driver.get_cookies()
domeinen = []

for array in cookies:
    domeinen.append(array.get("domain"))

print(domeinen)

for domein in domeinen:
    if not DOMAIN in domein:
        print(f'{{"name": "cookie", "score": 0, "message": "Uw website {url} maakt gebruik van third party cookies."}}')
        exit()
print(f'{{"name": "cookie", "score": 10, "message": "Uw website {url} maakt GEEN gebruik van third party cookies."}}')
