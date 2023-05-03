import sys,os,csv
sys.path.append(os.path.realpath('..'))

with open('csv/data.csv', 'r') as fin:
    data = list(csv.reader(fin))
with open('csv/data.csv', 'w', newline='') as fout:
    writer = csv.writer(fout)
    writer.writerows(data[1:])