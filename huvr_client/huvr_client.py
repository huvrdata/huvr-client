# -*- coding: utf-8 -*-

"""Main module."""

import json

import requests

from .__version__ import __version__ as VERSION


class Client(object):
    """ Client object is a simple wrapper around a requests Session. """

    def __init__(self, url, verbose=None):
        self.verbose = verbose
        self.base_url = url

    def login(self, username, password):
        """ Login and create a session """
        if username and password:
            self.credentials = {
                "email": username,
                "password": password,
            }
        else:
            username = self.credentials["email"]

        # use a Session to manage cookies
        self.client = requests.Session()
        headers = {"content-type": "application/x-www-form-urlencoded"}

        url = self.base_url + "/login"

        response = self.client.post(url, data=self.credentials, headers=headers)

        if response.status_code == 400:
            print("ERROR: please enter valid credentials")
            response.raise_for_status()
            exit()
        print("huvr_client: Logged {} in to {}".format(username, self.base_url))

    def post(self, url, data):
        """ Override the requests.post handler so that we can dynamically enable
        logging, with our verbose flag. """

        headers = {
            'User-Agent': 'huvr-api-client/{}'.format('0.1.0'),  # python-requests/2.22.0
        }

        if self.verbose:
            print("huvr_api_client: POSTING {}".format(url))
            print(json.dumps(data, indent=4))
        response = self.client.post(url, json=data, headers=headers)
        if self.verbose:
            print("huvr_api_client: {} {}".format(response.request.method, response.url))
        return response

    def get(self, url, params=None):
        """
        Override the requests.get handler so that we can dynamically enable
        logging, with our verbose flag.
        """
        headers = {
            "User-Agent": "huvr-client/{}".format(VERSION),
        }

        if self.verbose:
            print("huvr_client: Fetching {}".format(url))
        response = self.client.get(url, params=params, headers=headers)
        if self.verbose:
            print(
                "huvr_client: Fetched {} {}".format(
                    response.request.method, response.url
                )
            )
        return response

    def put(self, url, data={}):
        """
        Override the requests.put handler so that we can dynamically enable
        logging, with our verbose flag.
        """
        headers = {
            "User-Agent": "huvr-client/{}".format(VERSION),
        }

        if self.verbose:
            print("huvr_client: Putting {}".format(url))
            print(json.dumps(data, indent=4))
        response = self.client.put(url, json=data, headers=headers)
        if self.verbose:
            print(
                "huvr_client: Put {} {}".format(response.request.method, response.url)
            )
        return response

    def profiles(self, id=None):
        """
        Get profiles
        GET /api/profiles
        GET /api/profiles/<profile_id>
        """
        url = "{}/api/profiles".format(self.base_url)

        if id:
            url = "{}/{}".format(url, id)

        response = self.get(url)
        if response.status_code == 200:
            return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def set_checklist(self, project_id, checklist_id):
        """ 
        given a project ID and a checklist ID, set the checklist
        POST /api/checklist/set
        """
        url = "{}/api/checklist/set/{}/{}".format(self.base_url, project_id, checklist_id)
        
        response = self.post(url, {})
        if response.status_code == 200:
            return (200, response)
        else:
            return (response.status_code, response.text)

    def set_profile(self, project_id, profile_id):
        """ 
        given a project ID and a profile ID, set the profile
        POST /api/profile/set
        """
        url = "{}/api/profile/set/{}/{}".format(self.base_url, project_id, profile_id)
        
        response = self.post(url, {})
        if response.status_code == 200:
            return (200, response)
        else:
            return (response.status_code, response.text)

    def project(self, data):
        """ Get profiles
        POST /api/projects
        """
        url = "{}/api/projects".format(self.base_url)

        response = self.post(url, data)
        if response.status_code == 201:
            return (201, response.json())
        else:
            return (response.status_code, response.text)

    def upload_project_media(self, upload_project_id):
        """
        PUT /api/projects/<project_id>/media
        """

        media_directory = '/data-dir/site/project/media-h2'
        if not os.path.exists(media_directory):
            print("Project directory does not exist [{}]".format( media_directory ))
            exit()

        media_files = os.listdir(media_directory)
        session = self.client  # grab pre-authenticated session. our file post headers are unique
        # lets don't upload images to projects twice.
        url = self.base_url + "/api/projects/{}/media".format(upload_project_id)
        print("GET: [{}]".format(url))
        response = session.request("GET", url, data="", headers={})
        images_already_uploaded=False
        if response.status_code == 200:
            rjson = response.json()
            if rjson:
                if rjson['count'] > 0:
                    images_already_uploaded=True

        if images_already_uploaded:
            print("Looks like we have already uploaded media for {}: {}".format(proj.key.id(), proj.title))
        else:
            cnt = 0
            for image in media_files:

                print(image)
                timestamp_mseconds = int((datetime.datetime.now() - datetime.datetime.utcfromtimestamp(0)).total_seconds() * 1000)
                
                # call get to the blob interface to prep for file upload
                url = self.base_url + "/api/blob/url?{}".format(timestamp_mseconds) 
                print("GET: [{}]".format(url))
                response = session.request("GET", url, data="", headers={})

                if response.status_code == 200:
                    rjson = response.json()
                    if rjson:
                        print("Success")
                        if self.verbose:
                            print(json.dumps(rjson, indent=4))
                            print("random [{}] url [{}]".format(rjson['random'], rjson['url']))
                        image_filename = "%s/%s" % ( media_directory, image)
                        mime = magic.Magic(mime=True)
                        # https://stackoverflow.com/a/35974071/1184492
                        files = {'upload': (image, open(image_filename,'rb'), mime.from_file(image_filename))}
                        values = {'project': upload_project_id, 'name':'file', 'filename':image}

                        headers = {
                            'Content-Type': mime.from_file(image_filename)
                        }
                      
                        response = session.request("POST", rjson['url'], files=files, data=values)
                        if response.status_code == 200:
                            print("File Upload Success")
                        else:
                            print(response.status_code)
                            print(response.reason)

    def profiles_name_lookup(self, profile_name):
        """ This wraps the project_types query and search'es for a name string """
        (res_code, profiles) = self.profiles()
        if res_code == 200:
            for result in profiles["results"]:
                if result["title"].strip() == profile_name.strip():
                    return (res_code, result)

            return (404, {"message": "Not Found"})
        else:
            return (res_code, profiles)

    def get_defects_config(self, profile_id):
        """ Get defects config
        GET /api/defects_config/<profile_id>
        """
        url = "{}/api/defects_config/{}".format(self.base_url, profile_id)

        response = self.get(url)
        if response.status_code == 200:
            return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def get_defects_for_category(self, major, minor):
        """
        Get defects config
        GET /api/defect/category/<major>/<minor>
        """
        if not major:
            return (400, {"ERROR": "Category Major is required"})

        if major and minor:
            url = "{}/api/defect/category/{}/{}".format(self.base_url, major, minor)
        else:
            url = "{}/api/defect/category/{}".format(self.base_url, major)

        response = self.get(url)
        if response.status_code == 200:
            return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def media_for_project(self, project_id):
        """
        Get defects config
        GET /api/projects/<profile_id>/media
        """
        if not project_id:
            return (400, {"ERROR": "Project ID is required"})

        if project_id:
            url = "{}/api/projects/{}/media".format(self.base_url, project_id)

        response = self.get(url)
        if response.status_code == 200:
            return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def checklists(self, id=None):
        """
        Get checklists ( the original REST API endpoint )

        GET /api/checklists
        GET /api/checklists/<checklist_id>
        """
        url = "{}/api/checklists".format(self.base_url)

        if id:
            url = "{}/{}".format(url, id)

        response = self.get(url)
        if response.status_code == 200:
            return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def checklist_v2(self, id=None, download_csv=False):
        """
        Get checklists

        GET /api/v2/checklist/<checklist_id>
        GET /api/v2/checklist/<checklist_id>?download_csv=True
        """
        if not id:
            return (400, {"ERROR": "Checklist ID is required"})

        url = "{}/api/v2/checklist/{}".format(self.base_url, id)
        payload = {}
        if download_csv:
            payload["download_csv"] = True

        response = self.get(url, params=payload)
        if response.status_code == 200:
            if download_csv:
                return (
                    200,
                    response.content.decode("utf-8"),
                )  # response.content == a string/and or bytes and response.text == unicode
            else:
                return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def project_types(self, id=None):
        """ Get project_types
        GET /api/project_types
        GET /api/project_types/<project_type_id>
        """
        url = "{}/api/project_types".format(self.base_url)

        if id:
            url = "{}/{}".format(url, id)

        response = self.get(url)
        if response.status_code == 200:
            return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def project_type_name_lookup(self, project_type_name):
        """
            Searches for project_type by name.

            This wraps the project_types query
        """
        (res_code, projecttypes) = self.project_types()
        if res_code == 200:
            for result in projecttypes["results"]:
                if result["name"].strip() == project_type_name.strip():
                    return (res_code, result)

            return (404, {"message": "Not Found"})
        else:
            return (res_code, projecttypes)

    def project_type_project_ids(self, project_type_id):
        """
        Get project type projects metadata

        GET /api/project_type/<project_type_id>/projects_ids
        """
        url = "{}/api/project_type".format(self.base_url)
        if not project_type_id:
            return {"ERROR": "Project type ID is required"}

        url = "{}/{}/projects_ids".format(url, project_type_id)
        response = self.get(url)

        if response.status_code == 200:
            return (200, response.json())
        else:
            return (response.status_code, response.text)

    def project_defects(self, project_id, download_csv=False):
        """
        Get project defects for a single project

        GET /api/projects/<project_id>/defects
        GET /api/projects/<project_id>/defects?download_csv=True
        """
        if not project_id:
            return {"ERROR": "Project ID is required"}

        url = "{}/api/projects/{}/defects".format(self.base_url, project_id)
        payload = {}
        if download_csv:
            payload["download_csv"] = True

        response = self.get(url, params=payload)
        if response.status_code == 200:
            if download_csv:
                return (200, response.content.decode("utf-8"))
            else:
                return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def projects_meta(self, cursor_query=True):
        """
        Get projects metadata

        This is the cursor query request
        GET /api/projects_meta
        GET /api/projects_meta?offset=<cursor>
        """
        url = "{}/api/projects_meta".format(self.base_url)

        response = self.get(url)
        if response.status_code == 200:
            if cursor_query:
                total_results = []
                not_finished = True
                while not_finished:
                    data = response.json()
                    if "projects" in data:
                        total_results += data["projects"]
                    next_cursor = False
                    if "cursor" in data:
                        next_cursor = data["cursor"]
                    if next_cursor:
                        payload = {}
                        payload["offset"] = next_cursor
                        if self.verbose:
                            print(
                                "huvr_client: Fetched total {}".format(
                                    len(total_results)
                                )
                            )
                        response = self.get(url, params=payload)
                    else:
                        not_finished = False
                        return (200, total_results)
            else:
                return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def project_meta(self, project_id, download_csv=False):
        """
        Get projects metadata

        This is the cursor query request
        GET /api/projects_meta/<project_id>
        GET /api/projects_meta/<project_id>?download_csv=True
        """
        if not project_id:
            return {"ERROR": "Project ID is required"}

        url = "{}/api/projects_meta/{}".format(self.base_url, project_id)
        payload = {}
        if download_csv:
            payload["download_csv"] = True

        response = self.get(url, params=payload)
        if response.status_code == 200:
            if download_csv:
                return (200, response.content.decode("utf-8"))
            else:
                return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def asset_types(self, id=None):
        """
        Get asset_types

        GET /api/asset_types
        GET /api/asset_types/<asset_type_id>
        """
        url = "{}/api/asset_types".format(self.base_url)

        if id:
            url = "{}/{}".format(url, id)

        response = self.get(url)
        if response.status_code == 200:
            return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def asset_type_name_lookup(self, asset_type_name):
        """ This wraps the asset_types query and searches for a name string """
        (res_code, assettypes) = self.asset_types()
        if res_code == 200:
            for result in assettypes["results"]:
                if result["name"].strip() == asset_type_name.strip():
                    return (res_code, result)
            return (404, {"message": "Not Found"})
        else:
            return (res_code, assettypes)

    def asset_type_assets(self, asset_type_id):
        """ Get assets for asset type
        GET /api/asset_type/<asset_type_id>/assets
        """
        url = "{}/api/asset_type".format(self.base_url)
        if not asset_type_id:
            return {"ERROR": "Asset type ID is required"}

        url = "{}/{}/assets".format(url, asset_type_id)

        response = self.get(url)
        if response.status_code == 200:
            return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def asset_defects(self, asset_id, download_csv=False):
        """ Get asset defects
        GET /api/asset/<asset_id>/defects
        GET /api/asset/<asset_id>/defects?download_csv=True
        """
        url = "{}/api/asset".format(self.base_url)
        if not asset_id:
            return {"ERROR": "Asset ID is required"}

        url = "{}/{}/defects".format(url, asset_id)
        payload = {}
        if download_csv:
            payload["download_csv"] = True

        response = self.get(url, params=payload)
        if response.status_code == 200:
            if download_csv:
                return (200, response.text)
            else:
                return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def get_statuses(self):
        """ Get valid statuses
        GET /api/project/statuses
        """
        url = "{}/api/project/statuses".format(self.base_url)

        response = self.get(url)
        if response.status_code == 200:
            return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))

    def project_status(self, project_id, status=None, note=None):
        """ Update a project's status
        PUT /api/projects/<project_id>/status
        """
        url = "{}/api/projects/{}/status".format(self.base_url, project_id)

        if status:
            data = {"status": status}
            if note:
                data["note"] = note
            response = self.put(url, data=data)
        else:
            response = self.get(url)
        if response.status_code == 200:
            return (200, response.json())
        else:
            return (response.status_code, json.loads(response.text))
