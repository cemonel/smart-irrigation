fp = open('data/1.csv', 'r')
fw = open('data/1-lowered.csv', 'w')

filepath = 'data/1.csv'
with open(filepath) as fp:
   line = fp.readline()
   fw.write (line)
   line = fp.readline()
   cnt = 0
   while line:
        if cnt % 180 == 0:
           fw.write (line)
        line = fp.readline()
        cnt = cnt + 1