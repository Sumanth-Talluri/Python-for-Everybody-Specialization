fname = input("Please enter file name: ")

if len(fname) < 1:
    fname = "mbox-short.txt"

fhand = open(fname)

x = 0
hr_data = dict()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    line = line.split()
    time = line[5]
    hr = time.split(":")[0]
    if hr not in hr_data:
        hr_data[hr] = 1
    else:
        hr_data[hr] += 1

hr_data = sorted(hr_data.items())

for k, v in hr_data:
    print(k, v)
