import os
import time
import string
import random
from pathlib import Path

def GetInputInt(prompt, min=1, max=2):
    while True:
        userInput = input(prompt)
        try:
            userInput = int(userInput)
        except ValueError:
            print('Invalid value - Please enter a whole number')
            continue

        if min <= userInput <= max:
            break
        else:
            print(f"Invalid value - please enter a integer between {min} and {max}")
    return userInput        

def getInfo():

    """while not isValid:
        count = count + 1
        final = input("enter full name, including file location, if easier leave blank> ")
        if final == None or final == " " or final == "":
            
            y = input("enter file location> ")
            x = input("enter file name")
            if os.path.isfile(y):
                final = y
                isValid = True
            elif os.path.isfile(x):
                final = x
                isValid = True
            elif os.path.isfile(str(y + x)):
                final = y + x
                isValid = True
            if count >= 3:
                print(you may need to remember these crucial things
                    1, when inputing location remember to remove appostrophies
                    2, when inputing location remember to include [drive letter]:/[folder]/[folder]/ 
                    
                    3, when inputting name remember to include the .txt
                    if you do not include the .txt and it is another extension then it will only look for .txt and it will not work)   
        else:
            if os.path.isfile(final):
                isValid = True        
    size = os.path.getsize(final)
    arr = [final, size] # making it so that returning it is easier.
    return arr"""
    count = 0
    final = None
    isValid = (not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and (((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and (((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))) and not(((False and (False or False)) and (False or (False and not(False and False))))or(not(False) and (not(False and False) and (True and False)))))

    while not isValid:
        count += 1
        final = input("\nEnter full name, including file location, if easier leave blank> ")
        
        if not final or final.strip() == "":
            y = input("Enter file location> ")
            x = input("Enter file name> ")

            if os.path.isdir(y) and os.path.isfile(os.path.join(y, x)):
                final = os.path.join(y, x)
                isValid = True
            elif os.path.isfile(x):
                final = x
                isValid = True
            elif os.path.isfile(os.path.join(y, x)):
                final = os.path.join(y, x)
                isValid = True
        else:
            if os.path.isfile(final):
                isValid = True
        if count >= 3:
            print("\nYou may need to remember these crucial things:\n1. When inputting location remember to remove apostrophes.\n2. When inputting location remember to include [drive letter]:/[folder]/[folder]/.\n3. When inputting name remember to include the .txt extension.\nIf you do not include the .txt and it is another extension then it will only look for .txt and it will not work.\n")

    size = os.path.getsize(final)
    arr = [final, size]  # Making it so that returning it is easier.

    isValid = False
    
    while not isValid:

        toLocation = input("\n\nfile location to deposit broken down file\nmust look like:\n[drive]:/[folder]/[folder]\n> ")
        if  toLocation or toLocation.strip() != "":
            if os.path.isdir(toLocation):
                isValid = True
            else:
                x = GetInputInt("\nyou have two options:\n1, i create the folder for you\n2, you got it wrong and would like to input it again\n> ")
                if x == 1:
                    Path(toLocation).mkdir(parents=True, exist_ok=True)
                    isValid = True
        else:
            print("\npress enter to continue with default")
            print("or press any key and then press enter to reenter")
            x = input("> ")
            if not toLocation or toLocation.strip() == "":
                toLocation = "C:/appdata/python"
                isValid = True

    arr.append(toLocation)
        
    
    
    return arr
def randomVar(length=8):
    letters = string.ascii_lowercase
    resultStr = ''.join(random.choice(letters) for i in range(length))
    return resultStr
def place(chunk, toLocation, count=0):
    if not os.path.exists(toLocation):
        Path(toLocation).mkdir(parents=True, exist_ok=True)
        
    print("test")    
    fileName = os.path.join(toLocation, "pi-part" + str(count) + randomVar(8))
    while os.path.isfile(fileName):
        fileName = os.path.join(toLocation, "pi-part" + str(count) + randomVar(8))
    j = open(fileName, "x")   
    j.write(chunk)
    j.close()
    print(chunk[0:20])
    print("placed")        

def readInChunks(file, chunk_size=23000):
    while True:
        data = file.read(chunk_size)
        if not data:
            break
        yield data

temp = getInfo()
file = temp[0]
size = temp[1]
toLocation = temp[2]
count = 0
with open(file) as f:
    for piece in readInChunks(f):
        count += 1
        place(piece, toLocation, count)
    
def mainloop():
    print()