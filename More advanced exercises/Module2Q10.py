hw = float(input("Hourly wage:"))
rh = int(input("Regular hours:"))
oh = int(input("Overtime hours:"))
wp = (hw*rh) + ((hw*1.5)*oh)
print(wp)
