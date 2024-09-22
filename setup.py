import os
import json
from pathlib import Path

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
    while True:
        x = getInputInt(f"\nenter size of smaller files in bytes {bcolors.WARNING}(default= 50kb){bcolors.ENDC}\n> ", 1, fromFileSize-1, 50000)
        print(f"{bcolors.FAIL}as a safety measure, please make sure that you have more memory \nthan the size of each smaller file in bytes{bcolors.ENDC}")
        y = input(f"{bcolors.FAIL}press enter to contine: {bcolors.ENDC}")
        break
    return x        
def getToFolder(form):
    isValid = False
    toLocation = None
    while not isValid:

        toLocation = input(f"\n\nfile location to deposit broken down file\nmust look like:\n{bcolors.OKBLUE}[drive]:/[folder]/[folder]{bcolors.ENDC}\nor you could press {bcolors.OKBLUE}enter{bcolors.ENDC} for the same location\n> ")
        if not toLocation or toLocation.strip() == "":
            toLocation = os.path.dirname(form)
            print(toLocation)
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

    while True:
        count += 1
        print("please input the file that you would like to split")
        print(f"it should look like: {bcolors.OKBLUE}[drive]:/[folder]/[folder]/[file.suffex]{bcolors.ENDC}")
        print(f"or you could press {bcolors.OKGREEN}enter{bcolors.ENDC} to give the options: \n{bcolors.OKBLUE}[drive]:/[folder]/[folder]\n{bcolors.ENDC}and then {bcolors.OKBLUE}[file.suffex]{bcolors.ENDC}")
        final = input("\nEnter full file name, including file location, if easier leave blank (will get more options)> ")
        
        if not final or final.strip() == "":
            y = input(f"Enter file location {bcolors.OKBLUE}[drive]:/[folder]/[folder]\n{bcolors.ENDC}> ")
            x = input(f"Enter file name {bcolors.OKBLUE}[file.suffex]{bcolors.ENDC}> ")

            if os.path.isdir(y) and os.path.isfile(os.path.join(y, x)):
                final = os.path.join(y, x)
                print("file found, saved")
                break
            elif os.path.isfile(x):
                final = x
                print("file found, saved")
                break
            elif os.path.isfile(os.path.join(y, x)):
                final = os.path.join(y, x)
                print("file found, saved")
                break
        else:
            print(final)
            if os.path.isfile(final):
                print("file found, saved")
                break
            else:
                print("file was not correct :( please try again: \n")    
        if count >= 3:
            print("\nYou may need to remember these crucial things:\n1. When inputting location remember to remove apostrophes.\n2. When inputting location remember to include [drive letter]:/[folder]/[folder]/.\n3. When inputting name remember to include the .txt extension.\nIf you do not include the .txt and it is another extension then it will only look for .txt and it will not work.\n")
        
        else:
            print("file was not correct :( please try again: \n")
    print("")    
    return final
def getToTotal(fromFile):
    toLocation = getToFolder(fromFile)
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
            toLocation = [prefix, toLocation, suffix, randomAmmount]
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
                json.dump(data, ffile, indent=4)
                break

        else:
            print(f"file already exists,\nyou can find in {file} delete and press enter")   
            x = input("enter to continue>")
def remove(file=docFile):
    
    try: 
        
        os.remove(file)
        return True
    
    except FileNotFoundError:
        print("file not found ")
        return False    
def settings(prefix, toLocation, suffix, fromFile, fromFileSize, chunkSize, delete, randg):
    settings = {
        "prefix": prefix,
        "toLocation": toLocation,
        "suffix": suffix,
        "fromFile": fromFile,
        "fromFileSize": fromFileSize,
        "chunkSize": chunkSize,
        "delete": delete,
        "randomAmount": randg,
        "runNum": 0
    }
    return settings
def makeNew():

    while True:
        temp = False
        fromFile = getFromFile()
        for i in fromFile:
            if i == None:
                print("one of your answers was null, reenter \n")
            else:
                temp = True
        if temp:
            break        
                
    arr = getToTotal(fromFile)  
    prefix = arr[0]
    toLocation = arr[1]
    suffix = arr[2]
    randg = arr[3]
    fromFileSize = getSizeFile(fromFile)
    chunkSize = getSplitFileSize(fromFileSize)
    delete = deleteOldFileQuestion(fromFile)    
    # Store the settings
    x = settings(prefix, toLocation, suffix, fromFile, fromFileSize, chunkSize, delete, randg)
    
    create(docFile, x)
def mainloop():
    y = False
    while os.path.exists(docFile):
        print(f"setting file exists, do you want to delete it?")
        print(f"{docFile}")
        x = getInputInt("1, yes. 2, no> ")
        if x == 1:
            y = remove()
        else:
            print("just to confirm, you want to keep the file? ") 
            x = getInputInt("1, yes. 2, no> ")
            if x == 1:
                print("no need to run setup, just run splitting.py :) ")
                exit()
            else:
                y = remove()
    
    makeNew()


if __name__ == "__main__":
    mainloop()
    print(f"you can find the settings in {docFile}")
