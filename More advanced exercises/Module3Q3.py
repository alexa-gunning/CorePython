iHeight = float(input("Enter the initial height:"))
nrBounce = int(input("How many times can the ball bounce?"))
i = 1
tSum = iHeight + (iHeight*0.6)
while i <= nrBounce:
    iHeight = iHeight * 0.6
    tSum = tSum + iHeight
    i = i+1
print(tSum)
