read = input("Enter the file name to read from:")
write = input("Enter the file name to write to:")
r = open(read,'r')
w = open(write,'w')
i = 1
lines1 = r.readline()
for chars in lines1:
    lines = str(i) + ">" + lines1
    i = i+1
    w.write(lines)
    lines1 = r.readline()
w.close()
