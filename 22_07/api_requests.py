import requests


def all_posts():
    #response = requests.request("GET", "https://jsonplaceholder.typicode.com/posts")
    response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    assert len(response) == 99, "Not all posts have returned"

def one_post():
    post_id = new_post()
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}").json()
    assert response["id"] == post_id, "Not 42"

def post_a_post():
    body = {
        "title": "Test1",
        "body": "Test2",
        "userId": "asdasd"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST",
        "https://jsonplaceholder.typicode.com/posts",
        json= body,
        headers=headers
    )
    print(response.json())
    assert response.status_code == 201, "Status code is incorrect"
    assert response.json()["id"] == 101, "ID is incorrect"

def new_post():
    body = {
        "title": "Test1",
        "body": "Test2",
        "userId": "asdasd"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST",
        "https://jsonplaceholder.typicode.com/posts",
        json= body,
        headers=headers
    )
    return response.json()["id"]

def clear(post_id):
    response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")


def put_a_post():
    post_id = new_post()
    body = {
        "title": "Test1-UPD",
        "body": "Test2-UPD",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        json= body,
        headers=headers
    ).json()
    assert response["title"] == "Test1-UPD"
    clear(post_id)




def patch_a_post():
    post_id = new_post()
    body = {
        "body": "Test2-PATCHED",
        "userId": 7
    }
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        json= body,
        headers=headers
    ).json()
    print(response)
    clear(post_id)

def delete_a_post():
    post_id = new_post()
    response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    print(response.json())
    print(response.status_code)


# delete_a_post()
# patch_a_post()
#put_a_post()
#post_a_post()
#one_post()
#all_posts()
