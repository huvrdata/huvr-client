
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))

api_template = environment.get_template("api.py.jinja")
api_module_template = environment.get_template("api_module.py.jinja")
base_api_module_template = environment.get_template("base_api_module.py.jinja")
