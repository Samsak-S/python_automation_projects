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
        target_url = file.read().strip()
    
    driver = webdriver.Chrome(chrome_options, chrome_service, True)
    driver.get(target_url)

    with open("url_3.txt") as file:
        url_1st = file.read().strip()

    if driver.current_url == url_1st:
        element = wait_for_element(driver, '//*[@id="otherTile"]').click()
        print("Yes it is!")

    element = wait_for_element(driver, '//*[@id="i0116"]').send_keys("Samsak.S@centrica.com" + Keys.ENTER)
    #my_password = getpass.getpass("Enter your password:")
    element = wait_for_element(driver, '//*[@id="i0118"]').send_keys("Samsmithkezia31!" + Keys.ENTER)
    wait_for_element(driver, '//*[@id="signInAnotherWay"]').click()
    wait_for_element(driver, '//*[@id="idDiv_SAOTCS_Proofs"]/div[2]/div').click()
    my_pin = input("Enter your pin: ")
    wait_for_element(driver, '//*[@id="idTxtBx_SAOTCC_OTC"]').send_keys(my_pin + Keys.ENTER)

    
    shadow_1_host = wait_for_element(driver, '/html/body/macroponent-f51912f4c700201072b211d4d8c26010')
    shadow_1_root = driver.execute_script("return arguments[0].shadowRoot", shadow_1_host)

    shadow_2_host = shadow_1_root.find_element(By.CSS_SELECTOR, '#item-snCanvasAppshellMain')
    shadow_2_root = driver.execute_script("return arguments[0].shadowRoot", shadow_2_host)

    shadow_3_host = shadow_2_root.find_element(By.CSS_SELECTOR, 'div > sn-canvas-experience-shell > macroponent-c276387cc331101080d6d3658940ddd2')
    shadow_3_root = driver.execute_script("return arguments[0].shadowRoot", shadow_3_host)

    shadow_4_host = shadow_3_root.find_element(By.CSS_SELECTOR, '#item-wsContent')
    shadow_4_root = driver.execute_script("return arguments[0].shadowRoot", shadow_4_host)

    shadow_5_host = shadow_4_root.find_element(By.CSS_SELECTOR, 'main > sn-canvas-screen')
    shadow_5_root = driver.execute_script("return arguments[0].shadowRoot", shadow_5_host)

    time.sleep(2)

    shadow_6_host = shadow_5_root.find_element(By.CSS_SELECTOR, 'macroponent-4de8e06ff8a71110f8774f20ee1d6e6b')
    shadow_6_root = driver.execute_script("return arguments[0].shadowRoot", shadow_6_host)

    shadow_7_host = shadow_6_root.find_element(By.CSS_SELECTOR, '#item-express_list_1')
    shadow_7_root = driver.execute_script("return arguments[0].shadowRoot", shadow_7_host)

    shadow_8_host = shadow_7_root.find_element(By.CSS_SELECTOR, 'div > alerts-page')
    shadow_8_root = driver.execute_script("return arguments[0].shadowRoot", shadow_8_host)

    parent = shadow_8_root.find_element(By.CSS_SELECTOR, 'div.tabulator-table')

    child = parent.find_element(By.XPATH, './div[1]')
    children = parent.find_elements(By.CSS_SELECTOR, 'div.tabulator-cell')
    i = 0
    for small in children:
        if(i == 1):
            small.find_element(By.CSS_SELECTOR, 'div.formatterCell > div.alert-cell').click()
            time.sleep(5)
            print(driver.current_url)
        i += 1

    

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
