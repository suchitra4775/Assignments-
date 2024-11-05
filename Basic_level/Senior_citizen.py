birthyear = int(input("enter the birthyear:"))
currentyear = int(input("enter the currentyear:"))
Age=currentyear-birthyear
if(Age>=60):
    print("Senior Citizen")
else:
     print("Not Senior Citizen")