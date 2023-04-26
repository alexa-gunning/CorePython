import math
r = float(input("Enter the radius of the sphere:"))
d = 2*r
c = 2*math.pi*r
sa = 4*math.pi*r**2
v = 4/3*math.pi*r**3
print("Diameter:", str(d),"Circumpherence:", str(c), "Surface area:", str(sa), "Volume:", str(v))
