import random

response = "y"

while response == "y":
    no = random.randint(1,6)
    if(no == 1):
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        response = input("Enter ""y"" to continue or ""n"" to stop  ")
    elif(no==3):
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
        response = input("Enter ""y"" to continue or ""n"" to stop  ")
    elif(no==4):
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        response = input("Enter ""y"" to continue or ""n"" to stop  ")
    elif(no==5):
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        response = input("Enter ""y"" to continue or ""n"" to stop  ")
    elif(no==2):
        print("[-----]")
        print("[     ]")
        print("[0   0]")
        print("[     ]")
        print("[-----]")
        response = input("Enter ""y"" to continue or ""n"" to stop  ")
    elif(no==6):
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")
        response = input("Enter ""y"" to continue or ""n"" to stop  ")

 
