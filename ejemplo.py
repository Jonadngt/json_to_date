from json_to_date import module
import json_to_date
json_dir = 'person.json'
data = json_to_date.module.get_data(json_dir)

print('Nombre: ' + data.name)
print('Apellido: ' + data.last_name)
print('Cumpleaños: ' + data.birth)
print('Trabaja en: ' + data.job.name)
print('Comenzó a trabajar el: ' + data.job.start_date)
print('Autor: ' + json_to_date.__author__)