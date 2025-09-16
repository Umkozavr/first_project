from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3) #Purely for demonstration purposes

def test_id_name(driver):
    input_data = "kajshdkjasdkjasdk"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_string = driver.find_element(By.NAME, "text_string")
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result = driver.find_element(By.ID, "result-text")
    assert result.text == input_data

def test_classname(driver):
    input_data = "kajshdkjasdkjasdk"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_string = driver.find_element(By.CLASS_NAME, "textinput")
    #HTML could include multiple classes for 1 element. They are separated by spaces.
    #Always pick the unique class
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result = driver.find_element(By.CLASS_NAME, "result-text")
    print(result.text)
    print(result.get_attribute("innerText"))
    assert result.text == input_data

#Mostly used on headers
def test_tagname(driver):
    driver.get("https://www.qa-practice.com/elements/input/simple")
    assert driver.find_element(By.TAG_NAME, "h1").text == "Input field"

def test_link(driver):
    driver.get("https://www.qa-practice.com/elements/input/simple")
    contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, "act")

    #perform() activates the previously defined place to scroll
    ActionChains(driver).move_to_element(contact_link).perform()
    contact_link.click()

def test_css_selector(driver):
    driver.get("https://www.qa-practice.com/elements/input/simple")
    #text_string = driver.find_element(By.CSS_SELECTOR, '[placeholder="Submit me"]')
    text_string = driver.find_element(By.CSS_SELECTOR, '.form-control')
    text_string.send_keys("asdsadasdlsadlj")
    #text_string.send_keys(Keys.ENTER)
    print(text_string.value_of_css_property("border-color"))
    assert text_string.get_attribute("placeholder") == "Submit me"

def test_xpath(driver):
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_string = driver.find_element(By.XPATH, '//*[@id="id_text_string"]')
    text_string.send_keys("asdsadasdlsadlj")
    text_string.send_keys(Keys.ENTER)
