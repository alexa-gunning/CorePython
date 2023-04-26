theSum = 0.0
avg = 0.0
count = 0
data = input("Enter a number or just enter to quit:")
while data !="":
    num = float(data)
    theSum+=num
    count = count + 1
    data = input("Enter a number or just enter to quit:")
avg = theSum/count
print("Sum:",str(theSum), "Average:",str(avg))
