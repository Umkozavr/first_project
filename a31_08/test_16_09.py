from itertools import product

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    #chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3) #Purely for demonstration purposes

def test_input_clear(driver):
    input_data = "kajshdkjasdkjasdk"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_string = driver.find_element(By.NAME, "text_string")
    text_string.send_keys(input_data)
    text_string.clear()
    #In case clear() fails:
    # entered_value = text_string.get_attribute("value")
    # for _ in range(len(entered_value)):
    #     text_string.send_keys(Keys.BACKSPACE)
    assert text_string.is_displayed()

def test_enabled_and_select(driver):
    driver.get("https://www.qa-practice.com/elements/button/disabled")
    button = driver.find_element(By.NAME, "submit")
    print(button.is_enabled())
    dropdown_select = driver.find_element(By.ID, "id_select_state")
    dropdown = Select(dropdown_select)
    dropdown.select_by_value("enabled")

    print(button.is_enabled())

def test_waiting(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    button3 = driver.find_element(By.ID, "visibleAfter")
    button3.click()

def test_cart(driver):
    driver.get("https://www.next.pl/en/style/st628274/u84301#u84301")
    rej_cookies = driver.find_element(By.ID, "onetrust-reject-all-handler")
    rej_cookies.click()
    button_add = driver.find_element(By.CSS_SELECTOR, "div.pdp-css-u68e72")
    button_add.click()
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR,
         ".header-wo12yk  > .header-19xm0lj > .header-11yaxg4"),
        "1"))
    counter = driver.find_element(By.CSS_SELECTOR,
   ".header-wo12yk  > .header-19xm0lj > .header-11yaxg4")
    print(counter.text)

def test_5_sec_vis(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    (WebDriverWait(driver, 5).
     until(EC.presence_of_element_located(
     (By.ID, "visibleAfter"))))
    button3 = driver.find_element(By.ID, "visibleAfter")
    button3.click()
    driver.add_cookie({"name": "testname", "value": "testvalue"})
    print(driver.get_cookies())

def test_same_elements(driver):
    driver.get("https://www.next.pl/en/shop/home/bedding/duvets-and-pillows")
    rej_cookies = driver.find_element(By.ID, "onetrust-reject-all-handler")
    rej_cookies.click()
    product_link = driver.find_elements(By.CLASS_NAME, "produc-8adz9g")
    # product_link[0].click()
    print(product_link[0].find_element(By.CLASS_NAME, "MuiCardMedia-root").click())