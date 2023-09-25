from typing import TYPE_CHECKING

import requests
import os
import uuid

if TYPE_CHECKING:
    from .client import HuvrClient


def upload_inspection_media(
    client: "HuvrClient",
    filepath: str,
    project: int = None,
    checklist: int = None,
    **payload_kwargs,
):
    """
    Uploads a file to the HUVR API.

    :param client: The HUVR client.
    :param filepath: The path to the file to upload.
    :param project: The project ID to associate the file with. (optional)
    :param checklist: The checklist (form) ID to associate the file with. (optional)
    :param payload_kwargs: Additional keyword arguments to pass to the payload.
        see accepted values https://docs.huvrdata.app/reference/api_inspection-media_create
    :raises requests.HTTPError: If the upload fails.
    """

    filename = os.path.basename(filepath)

    payload = {
        "filename": filename,
        "file_meta": {"relative_path": filepath},
        "project": project,
        "checklist": checklist,
        **payload_kwargs,
    }

    # create the media record on HUVR
    inspection_media = client.inspection_media.create(json=payload)

    # signed url
    # allows the client to upload file directly to GCS
    signed_url = inspection_media["upload"]["url"]
    upload_headers = inspection_media["upload"]["headers"]

    with open(filepath, "rb") as file:
        upload_response = requests.put(signed_url, data=file, headers=upload_headers)
        # TODO - should be able to retry upload if it fails
        upload_response.raise_for_status()

    return inspection_media


def download_inspection_media(
    client: "HuvrClient",
    media_id: int,
    directory: str = ".",
    overwrite: bool = False,
):
    """
    Downloads a file from the HUVR API.

    :param client: The HUVR client.
    :param media_id: The ID of the file to download.
    :param directory: The directory to save the file to. (defaults to current directory)
    :param overwrite: Whether to overwrite the file if it already exists. (defaults to False)
    """

    # get the media record from HUVR
    inspection_media = client.inspection_media.read(id=media_id)

    # signed url
    # allows the client to download file directly from GCS
    signed_url = inspection_media["file"]

    # download the file
    response = requests.get(signed_url)
    filename = inspection_media["name"]
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath) and not overwrite:
        #   prevent overwriting files with the same name
        filename, extension = filename.split(".")
        filename = f"{filename}-{uuid.uuid4()}.{extension}"
        filepath = os.path.join(directory, filename)

    with open(filepath, "wb") as file:
        file.write(response.content)
