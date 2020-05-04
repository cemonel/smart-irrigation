file_number = 8
fw = open(f'low_sample_data/{file_number}.csv', 'w')

filepath = f'data/{file_number}.csv'
with open(filepath) as fp:
    line = fp.readline()
    fw.write(line)
    line = fp.readline()
    cnt = 0
    while line:
        if cnt % 360 == 0:
            fw.write(line)
        line = fp.readline()
        cnt = cnt + 1
