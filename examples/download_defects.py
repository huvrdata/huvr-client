#! /usr/bin/env python

"""
    Example to download project data into JSON or CSV files.
    Filter the data based on which project type(s) you are interested in.


    Change the url, username, password

    download_csv = True for CSV, False for JSON

    1. The script authorizes the client.
    2. Grabs the project types
    3. For earch project type, get all the projects
    4. Get all data related to each project
"""

import os
from huvr_client import Client
from huvr_client.helpers import make_base_directory, sanitize_name, write_csv_file, write_json_file, make_directory


if __name__ == '__main__':

    #  .-------------------------------.
    # |      Setup main variables       |
    #  '-------------------------------'
    url = "https://demo.huvrdatacloud.com"
    username = ""
    password = ""

    download_csv = True # use false to JSON

    base_directory = make_base_directory(os.getcwd(), "huvrdatacloud", "defects")
    debug_prints = False
    fetch_defects = True
    fetch_projects_metadata = True
    fetch_checklists = True

    # Login and go
    client = Client(url=url, verbose=True)
    client.login(username, password)


    # Set the project types you are intersted in
    project_type_names = [
        "Single Planetary Gearbox",
        "Double Planetary Gearbox",
        "GETS Gearbox",
        "Main Bearing",
        "Blade Inspection",
    ]

    fetch_project_types = {}
    (res_code, project_types) = client.project_types()
    if res_code == 200:
        for pt in project_types['results']:
            if pt["name"] in project_type_names:
                fetch_project_types[pt["id"]] = {"id": pt["id"], "name": pt["name"]}

    for pt_id in fetch_project_types.keys():
        # Set up directory to store stuff in
        project_type_directory_name = "{}/{}".format(base_directory, "_".join(fetch_project_types[pt_id]['name'].split()))
        make_directory(project_type_directory_name)

        final_defects = []
        final_defects_csv = u""

        final_projects_meta = []
        final_projects_csv = u""

        processing_project_cnt = 0
        final_checklist_csv = u""
        final_checklist_meta = []

        print("fetch project type defects for: {}".format(sanitize_name(fetch_project_types[pt_id]['name'])))
        (res_code_project_ids, project_ids) = client.project_type_project_ids(pt_id)
        if res_code_project_ids == 200:
            # print json.dumps(project_ids, indent=4)
            first_defect_line = True
            first_project_line = True
            first_checklist_line = True
            previous_checklist_meta_header_line_length = 0
            count = 0
            for project_id in project_ids:
                count += 1
                print("Processing project_id: {} of total: {} for ProjectType: {}".format(count, len(project_ids), sanitize_name(fetch_project_types[pt_id]['name'])))
                # ------------- F e t c h    D e f e c t s ----------
                if fetch_defects:
                    (res_code_defects, defects) = client.project_defects(project_id, download_csv=download_csv)
                    if res_code_defects == 200:
                        if defects:
                            if download_csv:
                                if first_defect_line and len(defects) > 0:
                                    first_defect_line = False
                                    final_defects_csv += u"{}".format(defects)
                                elif len(final_defects_csv.split('\n')) > 1 and len(defects.split('\n')) > 1:
                                    # trim the header line
                                    final_defects_csv += u"{} {}".format(u"\n".join(defects.split("\n")[1:]), "\n")

                                print(u"lines overall = {}".format(len(final_defects_csv.split('\n'))))
                                print(u"lines defects = {}".format(len(defects.split('\n'))))
                            else:
                                final_defects.append(defects['defects'])
                    else:
                        print("{} {}".format(res_code_defects, defects))

                if fetch_projects_metadata:
                    # ------------- F e t c h    P r o j e c t s    M e t a ----------
                    (res_code_pmeta, projects_meta) = client.project_meta(project_id, download_csv=download_csv)
                    if res_code_pmeta == 200:
                        if download_csv:
                            if first_project_line and len(projects_meta) > 0:
                                first_project_line = False
                                final_projects_csv += u"{}".format(projects_meta)
                            elif len(final_projects_csv.split('\n')) > 1 and len(projects_meta.split('\n')) > 1:
                                # trim the header line
                                final_projects_csv += u"{}".format(u"\n".join(projects_meta.split("\n")[1:]))

                            print(u"lines overall = {}".format(len(final_projects_csv.split('\n'))))
                            print(u"lines projects = {}".format(len(projects_meta.split('\n'))))
                        else:
                            final_projects_meta.append(projects_meta)

                    else:
                        print("{} {}".format(res_code_pmeta, projects_meta))

                if fetch_checklists:
                    if download_csv:
                        (res_code_pmeta, projects_meta) = client.project_meta(project_id, download_csv=False)

                    if 'project_id' in projects_meta and 'checklist_id' in projects_meta:
                        print("Project: {} has checklist_id: {}".format(projects_meta['project_id'], projects_meta['checklist_id']))
                        processing_project_cnt += 1
                        (res_code, checklist_meta) = client.checklist_v2(projects_meta['checklist_id'], download_csv=download_csv)
                        if res_code == 200:
                            if download_csv:
                                if first_checklist_line and len(checklist_meta) > 0:
                                    # trim the header line
                                    first_checklist_line = False
                                    # print len(checklist_meta)
                                    final_checklist_csv += u"{}".format(checklist_meta)
                                elif len(final_checklist_csv.split('\n')) > 1 and len(checklist_meta.split('\n')) > 1:
                                    # How long is the first line.
                                    current_checklist_meta_header_line_length = len(checklist_meta.split("\n")[0])
                                    if current_checklist_meta_header_line_length > previous_checklist_meta_header_line_length:
                                        # replace the first line
                                        final_cl_csv = final_checklist_csv.split("\n")
                                        final_cl_csv[0] = checklist_meta.split("\n")[0]
                                        final_checklist_csv = u"{}".format(u"\n".join(final_cl_csv))

                                    previous_checklist_meta_header_line_length = current_checklist_meta_header_line_length
                                    # final_checklist_csv += u"{} {}".format(u"\n".join(checklist_meta.split("\n")[1:]), "\n")
                                    final_checklist_csv += u"{}".format(u"\n".join(checklist_meta.split("\n")[1:]))

                                print(u"lines overall = {}".format(len(final_checklist_csv.split('\n'))))
                                print(u"lines checklists = {}".format(len(checklist_meta.split('\n'))))
                            else:
                                final_checklist_meta.append(checklist_meta)

            if fetch_defects:
                # ------------- F e t c h    D e f e c t s    S u m m a r y ----------
                if download_csv:
                    filename = "{}/{}_{}".format(project_type_directory_name, sanitize_name(fetch_project_types[pt_id]['name']), "defects.csv")
                    write_csv_file(filename, final_defects_csv)
                else:
                    filename = "{}/{}_{}".format(project_type_directory_name, sanitize_name(fetch_project_types[pt_id]['name']), "defects.json")
                    write_json_file(filename, final_defects)

            if fetch_projects_metadata:
                # ------------- F e t c h    P r o j e c t s    M e t a    S u m m a r y ----------
                if download_csv:
                    filename = "{}/{}_{}".format(project_type_directory_name, sanitize_name(fetch_project_types[pt_id]['name']), "projects.csv")
                    write_csv_file(filename, final_projects_csv)
                else:
                    filename = "{}/{}_{}".format(project_type_directory_name, sanitize_name(fetch_project_types[pt_id]['name']), "projects.json")
                    write_json_file(filename, final_projects_meta)

            if fetch_checklists:
                # ------------- F e t c h    P r o j e c t s    C h e c k l i s t    S u m m a r y ----------
                if download_csv:
                    filename = "{}/{}_{}".format(project_type_directory_name, sanitize_name(fetch_project_types[pt_id]['name']), "checklist_data.csv")
                    write_csv_file(filename, final_checklist_csv)
                else:
                    filename = "{}/{}_{}".format(project_type_directory_name, sanitize_name(fetch_project_types[pt_id]['name']), "checklist_data.json")
                    write_json_file(filename, final_checklist_meta)

        else:
            print("{} {}".format(res_code_project_ids, project_ids))
