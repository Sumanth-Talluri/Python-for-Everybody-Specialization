largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    else:
        try:
            numint = int(num)
            if smallest is None:
                smallest = numint
            elif numint < smallest:
                smallest = numint
            if largest is None:
                largest = numint
            elif numint > largest:
                largest = numint
        except:
            print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
