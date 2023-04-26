count = 0
sentence = input("Sentence:")
for character in sentence:
    if character == ' ':
        count = count + 1

print(count)
