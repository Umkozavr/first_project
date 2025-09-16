from locust import task, HttpUser

class TestUser(HttpUser):

    @task
    def get_all_stuff(self):
        self.client.get("https://www.webpagetest.org/")
