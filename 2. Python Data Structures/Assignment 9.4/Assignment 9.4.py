fname = input('Please enter file name: ')
fhand = open(fname)

data = dict()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    line = line.split()
    email = line[1]
    if email not in data:
        data[email] = 1
    else:
        data[email] += 1

maxx = None
maxx_key = None

for k in data:
    if maxx is None or maxx < data[k]:
        maxx = data[k]
        maxx_key = k


print(maxx_key, maxx)
