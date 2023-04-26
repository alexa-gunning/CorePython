a = float(input("Enter length of side 1:"))
b = float(input("Enter length of side 2:"))
c = float(input("Enter length of side 2:"))
ans = ""
if a == b and a == c:
    ans = "Equilateral"
else:
    ans = "Not Equilateral"
print(ans)
