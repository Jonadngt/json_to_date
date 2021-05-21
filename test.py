import json_to_date
from json_to_date import module
json_dir = 'person.json'
json_url = 'https://swapi.dev/api/people/'
data1 = module.get_from_file(json_dir)
data2 = module.get_from_url(json_url)
print(data1.name)
print(data2.count)