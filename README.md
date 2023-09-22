# HUVR Client

A Python client (with examples) to connect to HUVRdata.

You must be an active customer of HUVRdata.com for this library to be useful.

The client is a thin wrapper around the Python `requests` library. It is provided as
a convenience to help customers access their data.

See the https://docs.huvrdata.app for detailed specs on specific API endpoints.  Along with guides for most common use cases.

## Usage

### Installation

Use pip to install the client.   See pip/python installation best practices: https://docs.python-guide.org/starting/installation/

```bash
pip install huvr-client
```

### Client Initialization

You will need a service account in the HUVRdata platform to use this client.  Please contact your HUVRdata representative to get your credentials.

```py
from huvr_client import get_huvr_client

# Create a client with your credentials
client = get_huvr_client(
    base_url="https://demo.huvrdata.app",
    client_id="my-company.service-account@demo.huvrdata.app",
    client_secret="my-secret"
)
```

#### Authentication

The client will be authenticated for 1 hour.  After that, you will need to re-authenticate.

```py
client.authenticate(
    client_id="my-company.service-account@demo.huvrdata.app",
    client_secret="my-secret"
)
```

### Fetch Data Example

pass `params` to specify filters

_for full list of available filters - see [API docs](https://docs.huvrdata.app)_

```py
pagination_data = client.projects.list(params={
    "asset_search": "my-site/my-asset"
})

# some responses will contain pagination info {next, previous, count, results}
projects = pagination_data["results"]

# result data will be raw python dicts/lists etc
for project in projects:
    print(project["name"])
```

### Post Data Example

pass `json` to request when creating/updating data

_for full list of expected json data - see [API docs](https://docs.huvrdata.app)_

```py
project = client.projects.create(json={
    "name": "My Project",
    "asset": 24,  # asset id
    "type": 36,  # project type id
})

# result data will be raw python dicts/lists etc
print(project["id"])
```

### Raw Request Example

if requesting a non-json or "internal" endpoint, can make a raw request.

this will return a standard python `requests.Response` object

```py
response = client.request(
    method="GET",
    path="/api/.../",
    # params={...},
    # json={...},
    # headers={...},
    # data={...},
)
response.content  # access raw bytes, or .json(), etc
```

## Contributing / Internals

Docker Required: https://www.docker.com

### Run Codegen

All API endpoints are generated from the OpenAPI spec.

To regenerate the client code, first, obtain a link to the latest OpenAPI spec at https://docs.huvrdata.app/openapi/. Then run the following command:

```bash
make generate_client open_api_url="https://docs.huvrdata.app/openapi/<version>"
```

If a new _module_ is added to the spec, you will need to add it to the `huvr_client/client.py` file.

### Test

create a `tests/.env.yaml` file based on the `tests/.example.env.yaml` file.

```bash
make test
```

can also open a shell in the test container

```bash
make ipython
```

then:

```py
client = get_huvr_client(...)
```

### Publish

Generate a Release on GitHub.  This will trigger a GitHub Action to publish the package to PyPi.
