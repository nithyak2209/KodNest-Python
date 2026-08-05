marks=int(input("Enter your marks:"))
attendance=int(input("Enter your attendance percenatge:"))
project=input("Yes or No:")
if marks>=60 and attendance>=75 and projects=="Yes":
    print("Eligible")
else:
    print("Not Eligible")