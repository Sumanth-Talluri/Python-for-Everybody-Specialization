fname = input("Enter file name: ")
fh = open(fname)

count = 0
sum = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        val = float(line[-6:])
        sum += val

try:
    avg = sum/count
    print(f"Average spam confidence: {avg}")

except:
    print("No Lines Found")
