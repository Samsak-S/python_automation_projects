import getpass

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

from pathlib import Path

# The following modules are used for waiting for the site to load

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():

    file_path = Path("./chromedriver.exe").resolve()
    chrome_service = Service(file_path)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("disable-inforbars")
    chrome_options.add_argument("disable-dev-shm-usage")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("disable-blink-features=AutomationController")
    chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])

    url_path = Path("./url.txt").resolve()
    with open(url_path, "r") as file:
        target_url = file.read().split("\n")[1].strip()
    
    driver = webdriver.Chrome(chrome_options, chrome_service, True)
    driver.get(target_url)

    element = wait_for_element(driver, '//*[@id="otherTile"]').click()
    # driver.find_element(by="xpath", value='//*[@id="otherTile"]').click()
    print(driver.current_url)

    element = wait_for_element(driver, '//*[@id="i0116"]').send_keys("Samsak.S@centrica.com" + Keys.ENTER)
    my_password = getpass.getpass("Enter your password:")
    element = wait_for_element(driver, '//*[@id="i0118"]').send_keys(my_password + Keys.ENTER)
    wait_for_element(driver, '//*[@id="signInAnotherWay"]').click()
    wait_for_element(driver, '//*[@id="idDiv_SAOTCS_Proofs"]/div[2]/div').click()
    my_pin = input("Enter your pin: ")
    wait_for_element(driver, '//*[@id="idTxtBx_SAOTCC_OTC"]').send_keys(my_pin + Keys.ENTER)

    time.sleep(15)
    with open("output.txt","w") as file:
        file.write(driver.page_source)

    # parent_table = check_element(driver, '//*[@id="item-express_list_1"]')
    # children = parent_table.find_elements(By.CSS_SELECTOR, ".tabulator-row")

    # for child in children:
    #     print(child.text)

def check_element(driver, item_xpath):

    try:
        element = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH, item_xpath))
        )
    except:
        print("Timed out waiting for the page")

    return element

def wait_for_element(driver, item_xpath):

    try:
        element = WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, item_xpath))
        )
    except:
        print("Timed out waiting for the page")

    return element

def main():
    get_driver()

if __name__ == "__main__":
    main()
