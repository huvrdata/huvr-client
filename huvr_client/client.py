import re
import requests

from .api.api import Api


class HuvrClient:
    """
    REST API for HUVR.

    See full REST API documentation at https://docs.huvrdata.com
    """

    def __init__(
        self,
        base_url: str,
        verbose: bool = False,
    ):
        """
        Initialize the client.

        :param base_url: The base URL for the HUVR API. ex: https://demo.huvrdata.com
        :param verbose: print debug to stdout.
        """
        self.api = Api(self)
        self.base_url = base_url
        # remove trailing slash if present
        if self.base_url.endswith("/"):
            self.base_url = self.base_url[:-1]

        self.verbose = verbose
        self.session = requests.Session()

    def request(self, method: str, path: str, **kwargs) -> "requests.Response":
        url = self.base_url + path

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            **kwargs.pop("headers", {}),
        }

        if self.verbose:
            print(
                "HUVR HTTP REQUEST: {} {} {}".format(
                    method,
                    url,
                    {
                        "headers": headers,
                        **kwargs,
                    },
                )
            )

        return self.session.request(
            method,
            url,
            headers=headers,
            **kwargs,
        )

    def authenticate(self, client_id: str, client_secret: str):
        """
        Authenticate with the HUVR API.

        The access token is good for 60 minutes.  Then must re-authenticate.

        https://docs.huvrdata.app/docs/authentication
        """
        response = self.api.auth.obtain_access_token_create(
            json={
                "client_id": client_id,
                "client_secret": client_secret,
            }
        )
        response.raise_for_status()
        data = response.json()
        self.session.headers["Authorization"] = f"Token {data['access_token']}"


def get_huvr_client(base_url: str, client_id: str, client_secret: str) -> "HuvrClient":
    """
    Get an authenticated HUVR client.

    :param base_url: The base URL for the HUVR API. ex: https://demo.huvrdata.com
    :param client_id: The client ID for the HUVR API.
    :param client_secret: The client secret for the HUVR API.
    :return: An authenticated HUVR client.
    """
    client = HuvrClient(base_url)
    client.authenticate(client_id, client_secret)
    return client
