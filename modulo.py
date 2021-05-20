try:
    from modulo import settings
except:
    pass

import json

# Clase
class obj:
    # constructor
    def __init__(self, dict):
        self.__dict__.update(dict)

# Funcion
def get_data_from_json(path):
    """ Get the location of a json file and convert it to an object

    Receive
    ----------
    /path/file.json

    Return
    ----------
    object """
    with open(path) as file:
        data = json.load(file)
        obj_data = json.loads(json.dumps(data), object_hook=obj)
        return obj_data