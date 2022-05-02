import os
import sys
import json
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

SELENIUM_URL = os.environ.get("SELENIUM_URL")

if SELENIUM_URL is None or SELENIUM_URL == "":
    print("{}")
    exit()

def checkCookies(driver, target):
    """Test if DNSSEC is enabled for a specific domain.

    Args:
        driver (selenium.webdriver.Remote): The selenium web driver
        target (str): The target to check
    """

    url = 'http://' + target

    driver.get(url)

    time.sleep(5)

    cookies = driver.get_cookies()

    domeinen = []
    namen = []

    for array in cookies:
        namen.append(array.get("name"))
        domeinen.append(array.get("domain"))

    for domein in domeinen:
        if DOMAIN not in domein and domein not in DOMAIN:
            print(json.dumps({
                "name": "third party",
                "score": 0,
                "message": "The website loads third party cookies without consent."
            }))
            return

    print(json.dumps({
        "name": "third party",
        "score": 10,
        "message": "The website does not load third party cookies."
    }))

def main():
    """Main function
    """

    target = sys.argv[1]

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.set_capability("loggingPrefs", {'performance': 'ALL'})
    driver = webdriver.Remote(SELENIUM_URL + '/wd/hub', options=options)

    try:
        checkCookies(driver, target)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()
