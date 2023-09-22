import unittest
import yaml
import os

from huvr_client import HuvrClient, get_huvr_client
from huvr_client.media import upload_inspection_media, download_inspection_media

current_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_dir, ".env.yaml"), "r") as f:
    env = yaml.safe_load(f)

BASE_URL = env["BASE_URL"]
CLIENT_ID = env["CLIENT_ID"]
CLIENT_SECRET = env["CLIENT_SECRET"]


class TestClient(unittest.TestCase):
    def test_client_auth(self):
        client = get_huvr_client(BASE_URL, CLIENT_ID, CLIENT_SECRET)
        data = client.users.me_read()
        self.assertEqual(data["email"], CLIENT_ID)

    def test_media_upload(self):
        dirname = os.path.dirname(os.path.abspath(__file__))

        client = get_huvr_client(BASE_URL, CLIENT_ID, CLIENT_SECRET, verbose=True)
        media = upload_inspection_media(client, filepath=os.path.join(dirname, "image.png"))

        self.assertEqual(media["name"], "image.png")

        # delete file if it exists in "tmp" directory
        if os.path.exists(os.path.join(dirname, "tmp", "image.png")):
            os.remove(os.path.join(dirname, "tmp", "image.png"))
        download_inspection_media(client, media["id"], directory=os.path.join(dirname, "tmp"))

        self.assertTrue(os.path.exists(os.path.join(dirname, "tmp", "image.png")))
