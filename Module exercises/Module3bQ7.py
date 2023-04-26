x = int(input("Enter the first number:"))
op = input("Enter the operator:")
y = int(input("Enter the second number:"))
calc = 0
if op == '**':
        calc = x ** y
elif op == '-':
        calc = x = y
elif op == '*':
        calc = x*y
elif op == '-':
        calc = x-y
elif op == '%':
        calc = x%y
elif op == '+':
        calc = x+y
else:
     print("Operator invalid")

print(calc)

