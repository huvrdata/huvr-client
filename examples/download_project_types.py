#!/usr/bin/env python

import sys
import os
import json

from huvr_client import Client
from huvr_client.helpers import make_base_directory, save_profile_to_file, save_checklist_to_file, save_project_type_to_file


if __name__ == '__main__':
    #  .-------------------------------.
    # |      Setup main variables       |
    #  '-------------------------------'
    url = "https://demo.huvrdatacloud.com"
    username = ""
    password = ""

    base_directory = make_base_directory(os.getcwd(), "huvrdatacloud", "defects")


    #  .--------------------.
    # |  GET Project Types   |
    #  '--------------------'
    (res_code, project_types) = client.project_types()
    last_project_type_id = None
    if res_code == 200:
        # print json.dumps(project_types, indent=4)
        for project_type in project_types['results']:

            # Build up a directory for this ProjectType
            pt_name = "_".join(project_type['name'].split())
            working_directory = "{}/{}_{}".format(base_directory, pt_name, project_type['id'])
            if not os.path.exists(working_directory):
                print("Making Working Directory: [{}]".format(working_directory))
                os.makedirs(working_directory)

            try:
                profile_id = project_type['profiles'][-1]
                print("Fetching Profile [{}]".format(profile_id))
                (res_code, profile) = client.profiles(profile_id)
                if res_code == 200:
                    save_profile_to_file(profile, working_directory)
            except IndexError as e:
                print("No profile for Project Type {}".format(pt_name))

            try:
                checklist_id = project_type['checklists'][-1]
                print("Fetching Checklist [{}]".format(checklist_id))
                (res_code, checklists) = client.checklists(checklist_id)
                if res_code == 200:
                    save_checklist_to_file(checklists, working_directory)
            except IndexError as e:
                print("No checklist for Project Type {}".format(pt_name))

            save_project_type_to_file(project_type, working_directory)
