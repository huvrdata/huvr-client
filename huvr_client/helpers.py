import os
import json
import os.path
import io


def make_base_directory(cwd, path1, path2):
    base_directory = "{}/{}/{}".format(cwd, path1, path2)
    if not os.path.exists(base_directory):
        print("Making Base Directory: [{}]".format(base_directory))
        os.makedirs(base_directory)
    return base_directory


def make_directory(dir_name):
    if not os.path.exists(dir_name):
        print("Making Directory: [{}]".format(dir_name))
        os.makedirs(dir_name)


def write_csv_file(filename, data):
    with io.open(filename, "w", encoding="utf-8") as outfile:
        outfile.write(data)


def write_json_file(filename, data):
    with open(filename, "w") as outfile:
        outfile.write(json.dumps(data, indent=4))


def sanitize_name(name):
    return name.replace(" ", "_").replace(",", "_").replace("-", "_").replace("/", "_")


def save_profile_to_file(profile, working_directory):
    filename = "_".join(profile["results"]["settings"]["profile_name"].split())
    filename = sanitize_name(filename)
    filename = "profile_" + filename + ".json"
    filename = "{}/{}".format(working_directory, filename)
    with open(filename, "w") as outfile:
        tmp_json = {}
        tmp_json["settings"] = profile["results"]["settings"]
        outfile.write(json.dumps(tmp_json, indent=4))


def save_checklist_to_file(checklists, working_directory):
    filename = "_".join(checklists["json"]["metadata"]["checklist_name"].split())
    filename = sanitize_name(filename)
    filename = "checklist_" + filename + ".json"
    filename = "{}/{}".format(working_directory, filename)
    with open(filename, "w") as outfile:
        tmp_json = checklists["json"]
        if "archived" in tmp_json:
            del tmp_json["archived"]
            outfile.write(json.dumps(tmp_json, indent=4))


def save_project_type_to_file(project_type, working_directory):
    filename = "_".join(project_type["name"].split())
    filename = sanitize_name(filename)
    filename = "project_type_" + filename + ".json"
    filename = "{}/{}".format(working_directory, filename)
    with open(filename, "w") as outfile:
        outfile.write(json.dumps(project_type, indent=4))
