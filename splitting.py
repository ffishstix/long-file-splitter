import os
import time
import string
import random
from pathlib import Path

def getInputInt(prompt, min=1, max=2):
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

def getSizeFile(file):
    return os.path.getsize(file)
def getFromFile():
    count = 0
    final = None
    isValid = False
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
        if count >= 3 and not isValid:
            print("\nYou may need to remember these crucial things:\n1. When inputting location remember to remove apostrophes.\n2. When inputting location remember to include [drive letter]:/[folder]/[folder]/.\n3. When inputting name remember to include the .txt extension.\nIf you do not include the .txt and it is another extension then it will only look for .txt and it will not work.\n")
    return final       

def getToFile():
    isValid = False
    toLocation = None
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
            print(f"\npress enter to continue with default (C:/ProgramData/python)")
            print("or press any key and then press enter to reenter")
            x = input("> ")
            if not toLocation or toLocation.strip() == "":
                toLocation = "C:/ProgramData/python"
                isValid = True
    return toLocation                     

def getSplitFileSize(fromFile, fromFileSize):
    isValid = False
    while not isValid:
        x = getInputInt("\nenter size of smaller files> ", 1, fromFileSize-1)
        if x < fromFileSize:
            amountOfFiles = (fromFileSize // x) + 1
            print(f"there will be {amountOfFiles} files, is this ok? ")
            time.sleep(0.2)
            y = input("enter to continue, anything else to reenter> ")
            if  not y or y.strip() == "":
                isValid = True

            print(f"with {x} as the smaller file size there will be ")
        else:
            print(f"smaller file size cannot exceed original file size: {fromFileSize}")    
            print(f"you selected {x}, that is {x - fromFileSize} more than the original size")

    return x        
            


def getInfo():
    fromFile = getFromFile()
    fileSize = getSizeFile(fromFile)
    toLocation = getToFile()
    chunkSize = getSplitFileSize(fromFile, fileSize)
    arr = [fromFile, fileSize, toLocation, chunkSize]
    
    return arr

def randomVar(length=8):
    letters = string.ascii_lowercase
    resultStr = ''.join(random.choice(letters) for i in range(length))
    return resultStr
def place(chunk, toLocation, size, chunkSize, count=0):
    placements = int(size)//int(chunkSize)
    print(f"placements {placements} and count {count}")
    if placements == 1 and count==1:
        closeImediately = True
    else:
        closeImediately = False    
    if not os.path.exists(toLocation):
        Path(toLocation).mkdir(parents=True, exist_ok=True)
        
    print("test")    
    fileName = os.path.join(toLocation, "file" + str(count) + randomVar(8) + ".txt")
    while os.path.isfile(fileName):
        fileName = os.path.join(toLocation, "file" + str(count) + randomVar(8) + ".txt")
    j = open(fileName, "x")   
    j.write(chunk)
    
    if closeImediately or placements == count:
        print(f"closed {count}")
        j.close()
    #print(chunk[0:20])
    print(f"placed {count}")        

def readInChunks(file, chunkSize=32767):
    while True:
        data = file.read(chunkSize)
        if not data:
            break
        yield data

    
def mainloop():
    temp = getInfo()
    file = temp[0]
    size = temp[1]
    toLocation = temp[2]
    chunkSize = temp[3]
    count = 0
    with open(file) as f:
        for piece in readInChunks(f, chunkSize):
            count += 1
            place(piece, toLocation, size, chunkSize, count)

mainloop()
