from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_driver():

    file_path = Path('./chromedriver.exe').resolve()
    service = Service(file_path)

    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("--log-level=3") #Suppress most logs
    options.add_argument("disable-blink-features=AutomationController")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    url_path = Path('./url.txt').resolve()
    with open(url_path, 'r') as file:
        target_url = file.read().strip()

    driver = webdriver.Chrome(options=options, service=service)
    driver.get(target_url)
    return driver

def main():
    driver = get_driver()

main()