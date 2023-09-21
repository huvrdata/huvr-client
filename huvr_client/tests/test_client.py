import unittest
import yaml
from huvr_client import HuvrClient, get_huvr_client
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_dir, ".env.yaml"), "r") as f:
    env = yaml.safe_load(f)

BASE_URL = env["BASE_URL"]
CLIENT_ID = env["CLIENT_ID"]
CLIENT_SECRET = env["CLIENT_SECRET"]


class TestClient(unittest.TestCase):
    def test_client_auth(self):
        client = get_huvr_client(BASE_URL, CLIENT_ID, CLIENT_SECRET)
        response = client.users.me_read()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["email"], CLIENT_ID)
