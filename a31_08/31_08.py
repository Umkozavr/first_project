from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
#driver.maximize_window()
#driver.set_window_size(600, 700)
driver.get("https://www.google.com")

button_one = driver.find_element(By.ID, value="W0wltc")
button_one.click()

search_input = driver.find_element(By.NAME, value="q")
search_input.send_keys("cat")
search_input.send_keys(webdriver.Keys.ENTER)

assert "cat" in driver.title


sleep(3)



driver.quit()

