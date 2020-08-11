hrs = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hrs > 40:
    newrate = rate * 1.5
    pay = (40*rate) + (hrs-40)*newrate
else:
    pay = hrs*rate
print(f"Pay: {pay}")
