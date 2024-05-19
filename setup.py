import os
import json
from pathlib import Path
import psutil

# Define the directory and file path
USER_DOCUMENTS_DIR = Path.home() / 'Documents'
SETTINGS_DIR = USER_DOCUMENTS_DIR / 'ffishstix'
SETTINGS_FILE = SETTINGS_DIR / 'settings.fish'


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
            amountOfFiles = (fromFileSize // x) + 1
            last = fromFileSize% x
            print(f"there will be {amountOfFiles} files, at {x}bytes")
            print(f"apart from the last file which will be {last}bytes")
            
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
            print(f"\npress enter to continue with default (C:/ProgramData/python)")
            print("or press any key and then press enter to reenter")
            x = input("> ")
            if not toLocation or toLocation.strip() == "":
                toLocation = "C:/ProgramData/python"
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
def getToTotal():
    toLocation = getToFolder()
    isValid = False
    while not isValid:
        print("\nthe file wil look something like [prefix] 1,2,3... qaswdtres [suffix]")
        print("\nthis is because it allows more files to be generated without running into the same file name,\n the qaswdtres are random letters\n that are generated each loop\n leave blank for defaults:\nrandom ammount: 8\nsuffix: file\nprefix: .txt")
        randomAmmount = getInputInt("\nenter the length of random characters 2-16> ", 2, 16, 8)
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
def getSizeFile(file):
    return os.path.getsize(file)
def deleteOldFileQuestion(file): 
    return getInputInt(f"would you like to delete {file} after the split (default=no)\n1, no\n2, yes", 1, 2,1) == 2

 

def create(file, data):
    if not os.path.exists(file):
        with open(file, "w") as ffile:
            ffile.write(data)

    else:
        print("file already exists,\nyou can find in your documents/ffishstix/settings.fish delete and press enter")   
        x = input("enter to continue>")
        mainloop()
             


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
    fromFile = getFromFile()
    arr = getToTotal()
    prefix = arr[0]
    toLocation = arr[1]
    suffix = arr[2]
    fromFileSize = getSizeFile(fromFile)
    chunkSize = getSplitFileSize(fromFileSize)
    delete = deleteOldFileQuestion(fromFile)    
    chunkSize = getSplitFileSize()
    delete = deleteOldFileQuestion()

    # Store the settings
    settings(prefix, toLocation, suffix, fromFile, fromFileSize, chunkSize, delete)

    # Load and print all settings
    settings = load_settings()
    print("All settings:", settings)

    # Access and print specific settings
    print("Piece:", get_setting("piece"))
    print("To Location:", get_setting("toLocation"))
    print("Prefix:", get_setting("prefix"))
    print("Suffix:", get_setting("suffix"))
    print("Size:", get_setting("size"))
    print("Chunk Size:", get_setting("chunkSize"))