import requests


class HuvrApiError(requests.RequestException):
    """
    Base exception for HUVR API errors.
    """

    pass


class HuvrApiRequestError(HuvrApiError):
    """
    Exception for HUVR API request errors.
    """

    pass


class HuvrApiAuthError(HuvrApiError):
    """
    Exception for HUVR API authentication errors.
    """

    pass


class HuvrJSONResponseError(HuvrApiError):
    """
    Exception for HUVR API JSON response errors.
    """

    pass
