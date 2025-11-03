import re

from playwright.async_api import Page, expect, Request, Response, Route
from time import sleep
import json

def test_listen(page: Page):

    def print_request(request: Request):
        print('REQUEST:', request.post_data, request.url)

    page.on('request', print_request)
    page.on('response', lambda response: print('RESPONSE:', response.url, response.status))
    page.goto('https://www.qa-practice.com/')
    page.get_by_role('link', name='Text input').click()
    input_field = page.locator('#id_text_string')
    input_field.fill('asdsladasdl')
    input_field.press('Enter')

def test_catch_response(page: Page):
    page.goto('https://duckduckgo.com/')
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    with page.expect_response('**/stocks**') as response_event:
        search_field.press('Enter')

    response = response_event.value
    print(response.url)
    print(response.status)
    response_data = response.json()
    assert response_data['symbol'] == 'CAT'

def test_change_request(page: Page):

    def change_req(route: Route):
        url = route.request.url
        print(url)
        url = url.replace('&filter5=15p01', '')
        route.continue_(url=url)

    page.route(re.compile('/product/finder'), change_req)
    page.goto('https://www.samsung.com/au/smartphones/galaxy-z/')
    page.locator('[an-la="filter:Price"]').click()
    page.locator('.checkbox-v3__label-text', has_text='Below $500').click()
    sleep(3)

#No reason to do this
def test_API(page: Page):
    response = page.request.get('https://jsonplaceholder.typicode.com/posts/42')
    print(response.json(), response.status)
    expect(response).to_be_ok()
    assert response.json()['id'] == 42