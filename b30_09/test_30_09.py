from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3) #Purely for demonstration purposes


def test_scroll(driver):
    driver.get('https://the-internet.herokuapp.com/')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

def test_scroll_to_element(driver):
    driver.get('https://the-internet.herokuapp.com/')
    jquery_link = driver.find_element(By.LINK_TEXT, 'JQuery UI Menus')
    driver.execute_script('arguments[0].scrollIntoView();', jquery_link)
    jquery_link.click()
    #ActionChains(driver).move_to_element(jquery_link).click().perform()

def test_upload(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    upload = driver.find_element(By.ID, 'file-upload')
    submit = driver.find_element(By.ID, 'file-submit')
    upload.send_keys('C:/Users/Admin/Desktop/cat.jpg')
    submit.click()


