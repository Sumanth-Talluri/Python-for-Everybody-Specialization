fname = input('Please enter file name: ')
fhand = open(fname)

words = list()

for line in fhand:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word in words:
            continue
        else:
            words.append(word)

words.sort()
print(words)
