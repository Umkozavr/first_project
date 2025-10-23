from playwright.sync_api import Page, expect
import re
from time import sleep

def test_one(page: Page):
    page.goto('https://duckduckgo.com/')
    sleep(3)
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    search_field.press('Enter')
    expect(page).to_have_title(re.compile('^cat'))

def test_by_role(page: Page):
    page.goto('https://www.qa-practice.com/')
    sleep(3)
    contact_link = page.get_by_role('link', name='Contact')
    contact_link.click()
    expect(page).to_have_title(re.compile('^Contact Us'))

def test_by_text(page: Page):
    page.goto('https://www.qa-practice.com/')
    page.get_by_text('Single UI Elements').click()
    sleep(3)

def test_by_label(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    field = page.get_by_label('Text string')
    field.press_sequentially('This is a test message')
    sleep(1)
    field.press('Control+a')
    sleep(1)
    field.press('Backspace')
    sleep(3)

def test_by_placeholder(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    page.get_by_placeholder('Submit me').fill('By placeholder')
    sleep(3)

def test_by_alt_text(page: Page):
    page.goto('https://yourairtest.com/')
    page.get_by_alt_text('Ukrainian Hydrometeorological Institute').click()
    sleep(3)

#Shouldn't be used in real projects
def test_by_title(page: Page):
    page.goto('https://www.google.com/')
    page.get_by_role('button', name='Отклонить все').click()
    page.get_by_title('Поиск').fill('dog')
    sleep(3)

def test_by_test_id(page: Page):
    page.goto('https://practice.expandtesting.com/')
    sleep(3)
    page.get_by_test_id('build-version').click()
    sleep(3)

def test_by_css_selector(page: Page):
    page.goto('https://formy-project.herokuapp.com/dropdown')
    page.locator('#dropdownMenuButton').click()

def test_by_xpath(page: Page):
    page.goto('https://formy-project.herokuapp.com/dropdown')
    page.locator('//*[@id="navbarDropdownMenuLink"]').click()