import json

json_filename = '3'
csv_filename = '7'

with open(f'irrigation_data_as_json/{json_filename}.json', 'r') as f:
    datastore = json.load(f)

with open(f"data/{csv_filename}.csv", 'w') as f:
    f.write('time,soil_moisture,temperature,air_humidity' + '\n')
    for data in datastore['production']['data']:
        f.write(datastore['production']['data'][data] + '\n')
