import json

json_filename = '1'
csv_filename = '8'


with open(f"data/{csv_filename}.csv", 'w') as data:
    data.write('time,soil_moisture,temperature,air_humidity' + '\n')
    with open(f'database_irrigation_data_as_json/{json_filename}.json', 'r') as f:
        line = f.readline()
        line_as_json = eval(line)
        while line:
            data.write(str(line_as_json['epoch_time']) + ',' + str(line_as_json['soil_moisture']) + ',' + str(line_as_json['air_temperature']) + ',' + str(line_as_json['air_humidity']) +  '\n')
            line = f.readline()
            line_as_json = eval(line)

