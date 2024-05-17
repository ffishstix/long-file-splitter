import os
import time
import string
import random
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
        final = input("Enter full name, including file location, if easier leave blank> ")
        
        if not final or final.strip() == "":
            y = input("Enter file location> ")
            x = input("Enter file name> ")

            if not x or x.strip() == "" and not y or y.strip() == "":
                final = "C:/Users/finla/Downloads/y-cruncher v0.8.4.9538a/y-cruncher v0.8.4.9538a/Pi - Dec - Chudnovsky.txt" # me use only
                isValid = True
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
            print("""\nYou may need to remember these crucial things:
            1. When inputting location remember to remove apostrophes.
            2. When inputting location remember to include [drive letter]:/[folder]/[folder]/.
            3. When inputting name remember to include the .txt extension.
               If you do not include the .txt and it is another extension then it will only look for .txt and it will not work.\n""")

    size = os.path.getsize(final)
    arr = [final, size]  # Making it so that returning it is easier.
    
    return arr
def randomVar(length=8):
    letters = string.ascii_lowercase
    resultStr = ''.join(random.choice(letters) for i in range(length))
    return resultStr
def place(chunk, toLocation="C:/temp/python", count=0):
    if not os.path.exists(toLocation):
        if os.path.exists("C:"):
            os.mkdir(toLocation)
        else:
            print("programdata file does not exist, must be on windows and C:")
            time.sleep(0.5)
            exit(420)
    fileName = os.path.join(toLocation, "pi-part" + str(count) + randomVar(8))
    while os.path.isfile(fileName):
        fileName = os.path.join(toLocation, "pi-part" + str(count) + randomVar(8))
    j = open(fileName, "x")   
    j.write(chunk)
    j.flush()
    j.close()
    print(chunk[0:20])
    print("placed")        

def readInChunks(file="C:/Users/finla/Downloads/y-cruncher v0.8.4.9538a/y-cruncher v0.8.4.9538a/Pi - Dec - Chudnovsky.txt", chunk_size=23000):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 23k."""
    while True:
        data = file.read(chunk_size)
        if not data:
            break
        yield data

temp = getInfo()
file = temp[0]
size = temp[1]
count = 0
toLocation = "C:/temp/python"
with open(file) as f:
    for piece in readInChunks(f):
        count += 1
        place(piece, toLocation, count)
    
