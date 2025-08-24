# import unittest
# import requests
# import sys
#
#
#
# class TestPostApi(unittest.TestCase):
#
#
#     def setUp(self):
#         body = {
#             "title": "Test1",
#             "body": "Test2",
#             "userId": "asdasd"
#         }
#         headers = {"Content-Type": "application/json"}
#         response = requests.request("POST",
#                                     "https://jsonplaceholder.typicode.com/posts",
#                                     json=body,
#                                     headers=headers
#                                     )
#         self.post_id = response.json()["id"]
#         print(f"Post created: {self.post_id}")
#
#     def tearDown(self):
#         response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{self.post_id}")
#         print(f"Post deleted: {self.post_id}")
#
#     @unittest.skip("Getting an error every run")
#     def test_get_one_post(self):
#         response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{self.post_id}").json()
#         self.assertEqual(response["id"], self.post_id)
#
# class TestIndependent(unittest.TestCase):
#
#     @unittest.skipIf(sys.platform == "win32", "Not for Windows")
#     def test_get_all_posts(self):
#         response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
#         self.assertEqual(len(response), 100)
#
#     def test_add_post(self):
#         body = {
#             "title": "Test1",
#             "body": "Test2",
#             "userId": "asdasd"
#         }
#         headers = {"Content-Type": "application/json"}
#         response = requests.request("POST",
#                                     "https://jsonplaceholder.typicode.com/posts",
#                                     json=body,
#                                     headers=headers
#                                     )
#         print(response.json())
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.json()["id"], 101)
#
#
#
#
#
