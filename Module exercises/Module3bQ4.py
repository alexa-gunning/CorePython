digits = input("Digits:")
count = 0
for character in digits:
        if character == '0' or character == '1' or character == '2' or character == '3' or character == '4' or character == '5' or character == '6' or character == '7' or character == '8' or character == '9':
            count = count + 1

print(count)
