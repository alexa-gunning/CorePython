read = input("Enter the file name to read from:")
write = input("Enter the file name to write to:")
r = open(read,'r')
w = open(write,'w')
lines = r.read()
w.write(lines)
w.close()