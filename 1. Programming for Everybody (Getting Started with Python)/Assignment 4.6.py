h = float(input("Enter Hours: "))
r = float(input("Enter Rate: "))


def computepay(hrs, rate):
    if hrs > 40:
        return 40*rate + (hrs-40)*1.5*rate
    else:
        return hrs*rate


pay = computepay(h, r)
print(f"Pay: {pay}")
