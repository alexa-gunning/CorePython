iOrgs = int(input("Enter the initial nr of organisms:"))
rog = int(input("Enter the rate of growth (greater than 0):"))
hrs = int(input("Enter the number of hours to achieve this rate:"))
hrsG = int(input("Enter the number of hours for the population to grow:"))
prediction = iOrgs*rog*(hrsG/hrs)
print("The predicted population after", str(hrsG),"hours is", str(prediction))
