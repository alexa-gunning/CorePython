large = int(input("Enter the larger number:"))
small = int(input("Enter the smaller number:"))

while small != 0:
    a = large % small
    print("The remainder is:", str(a))
    large = small
    small = a
    print("The large number is now:",str(large),"The small number is now:",str(small))
