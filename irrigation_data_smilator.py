import time

filepath = 'low_sample_data/1.csv'

with open(filepath) as fp:
    fp.readline()
    line = fp.readline()
    cnt = 0
    while line:
        print(line)
        line = fp.readline()
        cnt = cnt + 1
        time.sleep(1)
