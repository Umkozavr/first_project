import requests
import pytest


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

@pytest.fixture()
def num():
    return 1