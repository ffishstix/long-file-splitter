import os
import time
import string
import random
import psutil
from pathlib import Path

def getMemoryAvaiable():
    return psutil.virtual_memory().available

def getSizeFile(file):
    return os.path.getsize(file)

def deleteOldFileQuestion(file): 
    return getInputInt(f"would you like to delete {file} after the split\n1, no\n 2, yes", 1, 2) == 1
def deleteOldFile(file):
    if os.path.exists(file):
        os.remove(file)
    else:
        print(f"could not find {file}\n possible reasons for this are:\n 1, the file is already deleted\n2, the file is corrupt")

def randomVar(length=8):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))        

def getInputInt(prompt, min=1, max=2):
    while True:
        userInput = input(prompt)
        try:
            userInput = int(userInput)
        except ValueError:
            if not userInput or str(userInput).strip() == "":
                userInput = min
                break
            else:
                print('Invalid value - Please enter a whole number')
                continue

        if min <= userInput <= max:
            break
        else:
            print(f"Invalid value - please enter a integer between {min} and {max}")
    return userInput        

def stringInFile(strSearch, filePath="fileExtensions.txt"):
    try:
        with open(filePath, 'r') as file:
            for line in file:
                if strSearch in line:
                    return True
        return False
    except FileNotFoundError:
        print(f"File {filePath} not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def getFromFile():
    count = 0
    final = None
    isValid = False
    while not isValid:
        count += 1
        print("please input the file that you would like to split")
        final = input("\nEnter full file name, including file location, if easier leave blank (will get more options)> ")
        
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

def getToFolder():
    isValid = False
    toLocation = None
    while not isValid:

        toLocation = input("\n\nfile location to deposit broken down file\nmust look like:\n[drive]:/[folder]/[folder]\n> ")
        if  toLocation or toLocation.strip() != "":
            if os.path.isdir(toLocation):
                isValid = True
            else:
                x = getInputInt("\nyou have two options:\n1, i create the folder for you\n2, you got it wrong and would like to input it again\n> ")
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

def getToTotal():
    toLocation = getToFolder()
    isValid = False
    while not isValid:
        print("\nthe file wil look something like [prefix] 1,2,3... qaswdtres [suffix]")
        print("\nthis is because it allows more files to be generated without running into the same file name,\n the qaswdtres are random letters\n that are generated each loop\n leave blank for defaults:\nrandom ammount: 8\nsuffix: file\nprefix: .txt")
        randomAmmount = getInputInt("\nenter the length of random characters 2-16> ", 2, 16)
        if not randomAmmount or str(randomAmmount).strip() == "":
            randomAmmount = 8    
        print("\nspecify file prefix")
        prefix = input("> ")
        if not prefix or prefix.strip() == "":
            print("default selected (file)")
        print("\n specify file suffix")        
        suffix = input("> ")
        if not suffix or suffix.strip() == "":
            print("default selected (.txt)")
        if stringInFile(suffix):
            toLocation = [prefix, toLocation, suffix]
            isValid = True
        else:
            isValid = False


    return toLocation        

def getSplitFileSize(fromFileSize):
    isValid = False
    while not isValid:
        x = getInputInt("\nenter size of smaller files in bytes> ", 1, fromFileSize-1)
        memory = getMemoryAvaiable()
        comp1 = x < fromFileSize
        comp2 = x < memory
        if comp1 and comp2:
            amountOfFiles = (fromFileSize // x) + 1
            print(f"there will be {amountOfFiles} files")
            time.sleep(0.2)
            y = input("enter to continue> ")
            if  not y or y.strip() == "":
                isValid = True

            
        else:
            if not comp1:

                print(f"smaller file size cannot exceed original file size: {fromFileSize}")    
                print(f"you selected {x}, that is {x - fromFileSize} more than the original size")
            if not comp2:
                print(f"make sure you have adequate memory: {memory/1000000000}GB's")

    return x        
    
def getInfo():
    while True: # should allow for more options

        fromFile = getFromFile()
        fileSize = getSizeFile(fromFile)
        toLocation = getToTotal()
        chunkSize = getSplitFileSize(fileSize)
        delete = deleteOldFileQuestion(fromFile)
        arr = [fromFile, fileSize, toLocation, chunkSize, delete]
        print(f"\n\n\n the file location of your large file: {fromFile}")
        time.sleep(0.4)
        print(f"\n\n the file location of your smaller file: {toLocation[1]}")
        time.sleep(0.4)
        print(f"\n\n the size of each smaller files: {chunkSize} bytes")
        time.sleep(0.4)
        print("\n if you are alright with this press enter")
        x = input("otherwise press anykey and then enter> ")
        if not x or x.strip() == "":
            break

    return arr

def place(chunk, toLocation, prefix, suffix, size, chunkSize, count=0):
    placements = int(size)//int(chunkSize)
    print(f"placements {placements} and count {count}")
    if placements == 1 and count==1:
        closeImediately = True
    else:
        closeImediately = False    
    if not os.path.exists(toLocation):
        Path(toLocation).mkdir(parents=True, exist_ok=True)
        
    print("test")    
    fileName = os.path.join(toLocation, f"{prefix}{str(count)}{randomVar(8)}{suffix}")
    while os.path.isfile(fileName):
        fileName = os.path.join(toLocation, f"{prefix}{str(count)}{randomVar(8)}{suffix}")
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
    arrtoLocation = temp[2]
    prefix = arrtoLocation[0]
    suffix = arrtoLocation[2]
    toLocation = arrtoLocation[1]
    chunkSize = temp[3]
    delete = temp[4]
    count = 0
    with open(file) as f:
        for piece in readInChunks(f, chunkSize):
            count += 1
            place(piece, toLocation, prefix, suffix, size, chunkSize, count)

    if delete:
        deleteOldFile(file)        
            
mainloop()

