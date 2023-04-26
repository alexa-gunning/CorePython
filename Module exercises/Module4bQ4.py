f = open("4bint.txt", 'r')
theSum = 0
count = 0
for line in f:
    numlist = line.split()
    for num in numlist:
        number = int(num)
        theSum += number
        count +=1
print(theSum/count)
