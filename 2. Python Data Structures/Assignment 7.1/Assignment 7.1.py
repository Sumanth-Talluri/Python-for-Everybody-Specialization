fname = input("Enter file name: ")
fh = open(fname)
content = fh.read()
print(content.upper().rstrip())
