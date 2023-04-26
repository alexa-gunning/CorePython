theSum = 0.0
while True:
    data = input("Enter a number or enter to quit:")
    if data == "":
        break
    number  = float(data)
    theSum = theSum + number
    print("Sum:",theSum)
    

