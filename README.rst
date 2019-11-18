HUVR Client
=========================================================

A Python client (with examples) to connect to HUVRdata.

You must be an active customer of HUVRdata.com for this library to be useful.

The client is a thin wrapper around the Python `requests` library. It is provided as
a convenience to help customers access their data.

To get started, install the client and try running the example code.


Examples
------------------------

You are now ready to run through our examples.
Edit this file :code:`download_defects.py` where you will modify several vars.
Go to the :code:`__main__` section of the code and change the:

  - :code:`url` to the your subdomain to run on
  - :code:`username` and :code:`password` for the appropriate user
  - :code:`project_type_names` list of project types to get
  - :code:`download_csv` set to true for CSV or false for JSON


This example script will create a directories for each project type. Inside the directory
it have a file for all the projects, the defects and the checklist data.

Now run it:

.. code-block:: bash

    $ ./download_defects.py
