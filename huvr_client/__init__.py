# -*- coding: utf-8 -*-

"""Top-level package for HUVR Client."""

from .__version__ import __title__, __description__, __url__, __version__  # noqa
from .__version__ import __build__, __author__, __author_email__, __license__  # noqa
from .__version__ import __copyright__  # noqa


from .huvr_client import Client

__all__ = [
    "Client",
]
