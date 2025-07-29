import time

import pytest
import requests
import allure


@pytest.fixture(scope="session")
def hello():
    print("Hello!")
    yield
    print("Bye")


@allure.feature("Posts")
@allure.story("Get posts")
@pytest.mark.skip
def test_get_one_post(new_post_id):
    with allure.step(f"Run get request for post with ID {new_post_id}"):
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{new_post_id}").json()
    with allure.step(f"Check that post ID is {new_post_id}"):
        assert response["id"] == new_post_id


@allure.feature("Posts")
@allure.story("Get posts")
@pytest.mark.smoke
def test_get_all_posts(hello):
    response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    assert len(response) == 100


@allure.feature("Posts")
@allure.story("Manipulate posts")
@pytest.mark.regression
def test_add_post():
    with allure.step("Prepare test data"):
        body = {
            "title": "Test1",
            "body": "Test2",
            "userId": "asdasd"
        }
        headers = {"Content-Type": "application/json"}
    with allure.step("Run request to create a post"):
        response = requests.request("POST",
                                    "https://jsonplaceholder.typicode.com/posts",
                                    json=body,
                                    headers=headers
                                    )
    with allure.step("Check that response code is 201"):
        assert response.status_code == 201
    with allure.step("Check that ID of the post is 201"):
        assert response.json()["id"] == 101


@allure.feature("Example")
@allure.story("Equals")
@pytest.mark.regression
def test_one():
    #time.sleep(3)
    assert 1 == 1


@allure.feature("Example")
@allure.story("Equals")
@pytest.mark.parametrize("logins", ["", "  ", ".,$@>#<@"])
def test_two(logins):
    print(logins)
    #time.sleep(3)
    assert 1 == 1


@allure.feature("Example")
@allure.story("Equals")
def test_three():
    #time.sleep(3)
    assert 1 == 1