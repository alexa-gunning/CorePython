text = input("Enter plain text:")
distance = int(input("Enter distance value:"))
ans = ""
for i in range(len(text)):
    ch = text[i]
    if ch==" ":
        ans+=" "
    elif(ch.isupper()):
        ans+=chr((ord(ch)+distance-65)%26+65)
    else:
        ans+=chr((ord(ch)+distance-97)%26+97)

print(ans)
