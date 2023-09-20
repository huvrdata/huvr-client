#! /usr/bin/env python3

import requests
import os
import re
import yaml

import templates
import utils


# go to https://docs.huvrdata.app/openapi/



def download_api_spec(api_spec_url):
    response = requests.get(api_spec_url)
    response.raise_for_status()
    spec = response.json()
    # for debugging, save the latest yaml for reference
    download_path = os.path.join(os.path.dirname(__file__), "spec/openapi.yaml")
    with open(download_path, "w") as f:
        yaml.dump(spec, f)
    return spec


class Endpoint:
    def __init__(self, module, method, path, method_name, docstring, url_replacements, has_query_params, has_body):
        self.module = module
        self.method = method
        self.path = path
        self.method_name = method_name
        self.docstring = docstring
        self.url_replacements = url_replacements
        self.has_query_params = has_query_params
        self.has_body = has_body

    def __repr__(self):
        return str(self.__dict__)


def prep_modules(spec: dict) -> dict:
    """
    Returns a dict of modules and their endpoints
    """
    modules = {
        # name: [endpoints]
    }

    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            if method == "parameters":
                continue

            module = utils.to_snake_case_from_kebob(details["tags"][0])

            operation_id = details["operationId"]

            # api_recommended-work-plans_update  -> update
            # api_schedule_plans_partial_update  -> plans_partial_update
            method_name = utils.to_snake_case_from_kebob(re.sub(r"^api_[^_]+_", "", details["operationId"]))

            # duplicate the operation names... get method for list
            # if method == "get" and "{id}" not in path:
            #     method_name = method_name.replace("get", "list")

            query_params = {}
            for parameter in details.get("parameters", []):
                if parameter["in"] == "query":
                    query_params[parameter["name"]] = parameter["schema"]["type"]

            body_schema = None
            if details.get("requestBody", {}).get("content"):
                body_schema = details["requestBody"]["content"]["application/json"]["schema"]
            elif details.get("requestBody", {}).get("$ref"):
                body_schema = details["requestBody"]

            response_schema = None
            try:
                response_schema = details["responses"]["200"]["content"]["application/json"]["schema"]
            except KeyError:
                pass
            try:
                response_schema = details["responses"]["201"]["content"]["application/json"]["schema"]
            except KeyError:
                pass


            docstring = details.get("description", "")
            docstring = docstring.split("------")[0]  # remove required perms -- too noisy
            docstring = docstring.replace("* Requires authentication.", "")  # inconsistent and noisy
            if query_params:
                docstring = docstring + f"\n:param dict params: {yaml.safe_dump(query_params)}"
            if body_schema:
                docstring = docstring + f"\n:param dict json: {yaml.safe_dump(body_schema)}"
            if response_schema:
                docstring = docstring + f"\n:returns: {yaml.safe_dump(response_schema)}"
            docstring = docstring.strip() + f"\n\nhttps://docs.huvrdata.app/reference/{operation_id}"
            docstring = utils.indent(docstring, 8).strip()

            url_replacements = []
            for param in re.findall(r"{[^}]+}", path):
                url_replacements.append(param[1:-1])

            if module not in modules:
                modules[module] = []

            # check no dupes
            for endpoint in modules[module]:
                if endpoint.method_name == method_name:
                    raise RuntimeError(f"Duplicate method: {module}.{method_name}")

            modules[module].append(
                Endpoint(
                    module=module,
                    method=method,
                    path=path,
                    has_query_params=bool(query_params),
                    has_body=bool(body_schema),
                    method_name=method_name,
                    docstring=docstring,
                    url_replacements=url_replacements,
                )
            )
    return modules


def generate_client(spec: dict):
    modules = prep_modules(spec)

    input("This will delete all files in ../huvr_client/api. Press enter to continue (or ctrl-c to cancel)...")

    # delete ../huvr_client dir
    os.system("rm -rf ../huvr_client/api")

    # make dirs if not exists
    os.makedirs("../huvr_client/api", exist_ok=True)

    # write __init__.py
    with open("../huvr_client/api/__init__.py", "w") as f:
        f.write("")

    # write base_module.py
    with open("../huvr_client/api/base_api_module.py", "w") as f:
        f.write(templates.base_api_module_template.render())

    for module_name, endpoints in modules.items():
        class_name = utils.to_pascal_case_from_snake(module_name)

        python_str = templates.api_module_template.render(
            docstring="todo",
            class_name=class_name,
            endpoints=endpoints,
        )

        with open(f"../huvr_client/api/{module_name}.py", "w") as f:
            f.write(python_str)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-u",
        "--api-spec-url",
        help="Go to https://docs.huvrdata.app/openapi/ to find the latest url (example: https://docs.huvrdata.app/openapi/63239c77e03070000fdc03d0)",
        required=True,
    )

    args = parser.parse_args()

    spec = download_api_spec(args.api_spec_url)

    generate_client(spec)
