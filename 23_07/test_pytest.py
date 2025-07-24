import pytest
import requests

@pytest.fixture()
def new_post_id():
    body = {"title": "Test1", "body": "Test2", "userId": "asdasd"}
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST",
                                "https://jsonplaceholder.typicode.com/posts",
                                json=body,
                                headers=headers
                                )
    post_id = response.json()["id"]
    yield post_id
    print("Deleting the post")
    requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")

@pytest.fixture(scope="session")
def hello():
    print("Hello!")
    yield
    print("Bye")

@pytest.mark.smoke
def test_get_one_post(new_post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{new_post_id}").json()
    assert response["id"] == new_post_id

@pytest.mark.smoke
def test_get_all_posts(hello):
    response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    assert len(response) == 100

@pytest.mark.regression
def test_add_post():
    body = {
        "title": "Test1",
        "body": "Test2",
        "userId": "asdasd"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST",
                                "https://jsonplaceholder.typicode.com/posts",
                                json=body,
                                headers=headers
                                )
    print(response.json())
    assert response.status_code == 201
    assert response.json()["id"] == 101

@pytest.mark.regression
def test_one():
    assert 1 == 1

@pytest.mark.parametrize("logins", ["", "  ", ".,$@>#<@"])
def test_two(logins):
    print(logins)
    assert 1 == 1

def test_three():
    assert 1 == 1