import os
import json
from pathlib import Path
import psutil

docDir = Path.home() / 'Documents' / 'ffishstix'
docFile = docDir / 'settings.fish'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
def getMemoryAvaiable():
    return psutil.virtual_memory().available
def getInputInt(prompt, min=1, max=2, default=min):
    while True:
        userInput = input(prompt)
        try:
            userInput = int(userInput)
        except ValueError:
            if not userInput or str(userInput).strip() == "":
                userInput = default
                break
            else:
                print(f'{bcolors.FAIL}Invalid value{bcolors.ENDC} - Please enter a whole number')
                continue

        if min <= userInput <= max:
            break
        else:
            print(f"{bcolors.FAIL}Invalid value{bcolors.ENDC} - please enter a integer between {min} and {max}")
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
def getSplitFileSize(fromFileSize):
    isValid = False
    while not isValid:
        x = getInputInt("\nenter size of smaller files in bytes> ", 1, fromFileSize-1, 50000)
        memory = getMemoryAvaiable()
        comp1 = x < fromFileSize
        comp2 = x < memory
        if comp1 and comp2:
            """amountOfFiles = (fromFileSize // x) + 1
            last = fromFileSize% x
            print(f"there will be {amountOfFiles} files, at {x}bytes")
            print(f"apart from the last file which will be {last}bytes")
            
            y = input("enter to continue> ")
            if  not y or y.strip() == "": ###### dont need this in setup
                isValid = True"""
            isValid = True
            
        else:
            # removed because the getIntInput already checks for this, should have realised sooner
            if not comp2:
                print(f"make sure you have adequate memory: {memory/1000000000}GB's")

    return x        
def getToFolder():
    isValid = False
    toLocation = None
    while not isValid:

        toLocation = input(f"\n\nfile location to deposit broken down file\nmust look like:\n{bcolors.OKBLUE}[drive]:/[folder]/[folder]{bcolors.ENDC}\n> ")
        if  toLocation or toLocation.strip() != "":
            if os.path.isdir(toLocation):
                isValid = True
            else:
                x = getInputInt("\nyou have two options:\n1, i create the folder for you\n2, you got it wrong and would like to input it again\n> ", 1, 2, 1)
                if x == 1:
                    Path(toLocation).mkdir(parents=True, exist_ok=True)
                    isValid = True
        else:
            print(f"\npress enter to continue with default ({docDir})")
            print("or press any key and then press enter to reenter")
            x = input("> ")
            if not x or x.strip() == "":
                toLocation = f"{docDir}"
                isValid = True
                
    return toLocation                     
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
            print(final)
            if os.path.isfile(final):
                isValid = True
        if count >= 3 and not isValid:
            print("\nYou may need to remember these crucial things:\n1. When inputting location remember to remove apostrophes.\n2. When inputting location remember to include [drive letter]:/[folder]/[folder]/.\n3. When inputting name remember to include the .txt extension.\nIf you do not include the .txt and it is another extension then it will only look for .txt and it will not work.\n")
    return final
def getToTotal(fromFile):
    toLocation = getToFolder()
    fromExtension = os.path.splitext(fromFile)[1]
    isValid = False
    while not isValid:
        print("\nthe output file wil look something like [prefix] 1,2,3... qaswdtres [suffix]")
        print(f"\nthis is because it allows more files to be generated without running into the same file name,\n the qaswdtres are random letters\n that are generated each loop\n leave blank for defaults:\nrandom ammount: 8\nsuffix: file\nprefix: {fromExtension}")
        randomAmmount = getInputInt("\nenter the length of random characters 2-16> ", 2, 16, 8)
        if not randomAmmount or str(randomAmmount).strip() == "":
            randomAmmount = 8    
            print(f"default selected ({randomAmmount})")

        print("\nspecify file prefix")
        prefix = input("> ")
        if not prefix or prefix.strip() == "":
            print("default selected (file)")
            prefix = "file"

        print("\n specify file suffix")        
        suffix = input("> ")
        if not suffix or suffix.strip() == "":
            print("default selected (.txt)")
            
            suffix = f"{fromExtension}"
        if stringInFile(suffix):
            toLocation = [prefix, toLocation, suffix]
            isValid = True
        else:
            isValid = False

    return toLocation        
def getSizeFile(file):
    return os.path.getsize(file)
def deleteOldFileQuestion(file): 
    return getInputInt(f"would you like to delete {file} after the split (default=no)\n1, no\n2, yes\n> ", 1, 2,1) == 2
def create(file, data):
    while True:
        if not os.path.exists(file):
            docDir.mkdir(parents=True, exist_ok=True)
            with open(file, "w") as ffile:
                ffile.write(str(data))
                break

        else:
            print(f"file already exists,\nyou can find in {file} delete and press enter")   
            x = input("enter to continue>")
        
def settings(prefix, toLocation, suffix, fromFile, fromFileSize, chunkSize, delete):
    settings = {
        "prefix": prefix,
        "toLocation": toLocation,
        "suffix": suffix,
        "fromFile": fromFile,
        "fromFileSize": fromFileSize,
        "chunkSize": chunkSize,
        "delete": delete
    }
    return settings
def get_setting(file, key):
    settings = open(file,"r")
    return settings.get(key)
def mainloop():
    
    while os.path.exists(docFile):
        print(f"setting file exists, you must delete before continuing")
        print("")
        print(docFile)
        x = input()
        

    fromFile = getFromFile()
    for i in fromFile:
        if i == None:
            print("one of your answers was null, reenter")
    arr = getToTotal(fromFile)  
    prefix = arr[0]
    toLocation = arr[1]
    suffix = arr[2]
    fromFileSize = getSizeFile(fromFile)
    chunkSize = getSplitFileSize(fromFileSize)
    delete = deleteOldFileQuestion(fromFile)    
    # Store the settings
    x = settings(prefix, toLocation, suffix, fromFile, fromFileSize, chunkSize, delete)
    
    create(docFile, x)
mainloop()
print(f"you can find the settings in {docFile}")
