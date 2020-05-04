import time
THRESHOLD_VALUE = 250

last_five_threshold_data = []

filepath = 'low_sample_data/1.csv'


def irrigation_signal():
    print("Irrigation signal SENT.")


with open(filepath) as fp:

    fp.readline()
    line = fp.readline()
    cnt = 0

    while line:
        print(line)
        soil_moisture = int(line.split('/t')[1])

        if soil_moisture < THRESHOLD_VALUE:
            last_five_threshold_data.append(soil_moisture)
        else:
            del last_five_threshold_data[:]

        if len(last_five_threshold_data) == 5:
            irrigation_signal()
            time.sleep(300)
        line = fp.readline()
        cnt = cnt + 1

