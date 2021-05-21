try:
    from json_to_date import settings
except:
    pass

import json
import requests

# Class
class obj:
    # constructor
    def __init__(self, dict):
        self.__dict__.update(dict)

# Functions
def _get(dict):
    """
    Get a dictionary and convert it to an object 
    """
    obj_data = json.loads(json.dumps(dict), object_hook=obj)
    return obj_data

def get_from_file(path):
    """
    Usage
    -----------------
    File to date:
    >>> import json_to_date
    >>> dir = "path/file.json"
    >>> data = json_to_date.module.get_from_file(dir)
    >>> print("Key value: " + data.<key>)
    Key value: value 
    """
    with open(path) as file:
        data = json.load(file)
        obj_data = _get(data)
        return obj_data

def get_from_url(url):
    """
    Usage
    -----------------
    URL to date:
    >>> import json_to_date
    >>> url = "https://jsondata.dev/api/user/1/"
    >>> data = json_to_date.module.get_from_url(url)
    >>> print("Key value: " + data.<key>)
    Key value: value
    """
    data_raw = requests.get(url)
    data = json.loads(data_raw.text)
    obj_data = _get(data)
    return obj_data