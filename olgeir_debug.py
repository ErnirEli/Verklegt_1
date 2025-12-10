from datetime import *

dob = input("Year/month/day: ")
dob = dob.split("/")
print(dob[1])
dob = date(int(dob[0]), int(dob[1]), int(dob[2]))

today = datetime.today().date()
age = today - dob

age = (age/365.25).days
print(age)
if age < 18:
    print("Ungur")
elif age > 99:
    print("Gamall")
else:
    print("rétt")            
