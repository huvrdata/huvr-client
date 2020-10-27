#!/usr/bin/env python

import sys
import os
import json

from huvr_client import Client


if __name__ == '__main__':
    #  .-------------------------------.
    # |      Setup main variables       |
    #  '-------------------------------'
    url = "https://patternenergy.testing.huvrdata.dev"

    # Login and go
    client = Client(url=url, verbose=True)
    client.login("support@huvrdatacloud.com", "")


    client.upload_project_media(6658551186456576, "media-h2/foo.jpg")

