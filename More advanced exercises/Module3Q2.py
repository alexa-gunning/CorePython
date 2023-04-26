a = float(input("Enter length of side 1:"))
b = float(input("Enter length of side 2:"))
c = float(input("Enter length of side 2:"))

if a**2 == (b**2)+(c**2) or b**2 == (c**2)+(a**2) or c**2 == (b**2)+(a**2):
    ans = "Right angle"
else:
    ans = "Not right angle"
print(ans)
