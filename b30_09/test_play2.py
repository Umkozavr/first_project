from playwright.async_api import BrowserContext, Page, expect, Dialog
from time import sleep

def test_visible(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    reqs = page.locator('#req_text')
    expect(reqs).not_to_be_visible()
    expect(reqs).to_be_hidden()
    page.locator('#req_header').click()
    expect(reqs).to_be_visible()
    sleep(2)


def test_enabled_and_select(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/disabled')
    button = page.locator('#submit-id-submit')
    expect(button).to_be_disabled()
    page.locator('#id_select_state').select_option('Enabled')
    expect(button).to_be_enabled()
    expect(button).to_contain_text('ubm')

def test_value(page: Page):
    text = 'some text'
    page.goto('https://www.qa-practice.com/elements/input/simple')
    input_field = page.locator('#id_text_string')
    input_field.fill(text)
    expect(input_field).to_have_value(text)

def test_sort_and_wait(page: Page):
    page.goto('https://www.saucedemo.com/v1/inventory')
    product_label = page.locator('.product_label')
    expect(product_label).not_to_be_empty()
    first_entry = page.locator('.inventory_item_name').locator('nth=0')
    print(first_entry.inner_text())
    page.locator('.product_sort_container').select_option(value='lohi')
    expect(page).to_have_url()
    print(first_entry.inner_text())
    sleep(5)

def test_focused(page: Page):
    page.goto('https://www.google.com/')
    page.locator('#W0wltc.tHlp8d').click()
    field = page.locator('[name="q"]')
    field.click()
    sleep(3)
    expect(field).to_be_focused()


def test_new_tab(page: Page, context: BrowserContext):
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/new_tab/link')
    link = page.locator('#new-page-link')
    with context.expect_page() as new_page_event:
        link.click()

    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    new_page.close()
    page.get_by_role('link', name='New tab button').click()
    sleep(3)

# def test_hover(page: Page):
#     page.goto('https://www.apple.com/')
#     sleep(3)
#     iphones = page.locator('.globalnav-link-iphone')
#     iphone_pro = page.locator('globalnav-submenu-link', has_text='iphone 17 pro')
#     iphones.hover()
#     sleep(3)
#     iphone_pro.click()

# def test_drag_and_drop(page: Page): #Doesn't work. Should be implemented via mouse actions
#     sleep(3)
#     page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
#     drag_me = page.locator('#rect-draggable')
#     drop_here = page.locator('rect-droppable')
#     drag_me.drag_to(drop_here)
#     sleep(3)

def test_alerts(page: Page):

    def cancel_alert(alert: Dialog):
        print(alert.message)
        print(alert.type)
        alert.dismiss()

    def fill_and_accept(alert: Dialog):
        alert.accept('Some text')

    # page.on('dialog', fill_and_accept)
    page.on('dialog', lambda alert: alert.accept('Another text'))
    page.goto('https://www.qa-practice.com/elements/alert/prompt')
    page.get_by_role('link', name='Click').click()
    sleep(3)
