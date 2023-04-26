f = open("myfile.txt", 'r')
count = 0
for line in f:
    wordlist = line.split()
    for word in wordlist:
        if len(word) == 4:
            print(word)
