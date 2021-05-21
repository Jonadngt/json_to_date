# Doc
""" 
json_to_date library
----------------- 
json_to_date is a module written in Python whose function is to receive data in 
json format and convert it into objects to facilitate the return of data.

Usage
-----------------
File to date:
>>> import json_to_date
>>> dir = "path/file.json"
>>> data = json_to_date.module.get_from_file(dir)
>>> print("Key value: " + data.<key>)
Key value: value

...

URL to date:
>>> import json_to_date
>>> url = "https://jsondata.dev/api/user/1/"
>>> data = json_to_date.module.get_from_url(url)
>>> print("Key value: " + data.<key>)
Key value: value
"""

# Module info
__author__ = "Jonathan Navarro"
__email__ = "jonadngt@gmail.com"
__version__ = "0.1.0"

# Load functions
from .module import(
    get_from_file,
    get_from_url
)