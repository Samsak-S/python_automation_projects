from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from pathlib import Path

def get_driver():

    get_src = Path("./chromedriver.exe").resolve()
    chrome_service = Service(get_src)

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("disable-dev-shm-usage")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("disable-blink-features=AutomationController")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(chrome_options, chrome_service, True)

    url_file = Path("./url_2.txt").resolve()

    with open(url_file, "r") as file:
        target_url = file.read().strip()

    driver.get(target_url)

    print(driver.current_url)

    driver.find_element(by="id", value="id_username").send_keys("automated")
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated"+ Keys.RETURN)

    driver.find_element(by="xpath", value="/html/body/nav/div/div/ul/li[2]/a").click()

    print(driver.current_url)
    
    title = driver.find_element(by="xpath", value="/html/body/div[1]/h1[1]")
    return title

def main():
    title = get_driver()
    print(title.text)

    
if __name__ == '__main__':
    main()