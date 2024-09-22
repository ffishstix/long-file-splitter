import os
import time
import string
import random
import ast
import json
from pathlib import Path
global bcolors
start = time.time()
docDir = Path.home() / 'Documents' / 'ffishstix'
docFile = Path.home() / 'documents' / 'ffishstix' / 'settings.fish'

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



def loadSettings(file):
    with open(file, 'r') as f:
        return json.load(f)

def saveSettings(file, data):
    """Save settings back to a JSON file."""
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def randomVar(length=8):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def place(chunk, toLocation, prefix, suffix, rand, runNum, count=0):    
    
    if not os.path.exists(toLocation):
        Path(toLocation).mkdir(parents=True, exist_ok=True)
    
    fileName = os.path.join(toLocation, f"{str(runNum) + prefix}{str(count)}{rand}{suffix}")
    while os.path.isfile(fileName):
        fileName = os.path.join(toLocation, f"{str(runNum) + prefix}{str(count)}{rand}{suffix}")
    with open(fileName, "x") as file:
        file.write(chunk)
      

def readInChunks(file, chunkSize=32767):
    while True:
        data = file.read(chunkSize)
        if not data:
            break
        yield data
    
def deleteOldFile(file):
    if os.path.exists(file):
        os.remove(file)
        print(f"{file} removed")
    else:
        print(f"could not find {file}\n possible reasons for this are:\n 1, the file is already deleted \n 2, the file is corrupt\n> ")        
def finish(start):
    end = time.time()
    print(f"operation finished:\n total time taken = {round((end-start),2)} seconds")
    x = input("press enter to continue> ")     
def mainloop():
    if os.path.exists(docFile):
        setting = loadSettings(docFile)
        prefix = setting["prefix"] 
        toLocation = setting["toLocation"]
        suffix = setting["suffix"]
        fromFile = setting["fromFile"]
        fromFileSize = setting["fromFileSize"]
        rands = setting["randomAmount"]
        chunkSize = setting["chunkSize"]
        delete = setting["delete"]
        runNum = setting["runNum"]
    else:
        print("run setup.py and rerun")
        exit(0)
    count = 0
    clear = lambda: os.system('cls')
    clear()
    print(f"process started (ctrl + c to cancel), bar below: ")
    rand = randomVar(rands)
    with open(fromFile) as f:
            for piece in readInChunks(f, chunkSize):
                count+=1
                place(piece, toLocation, prefix, suffix, rand, runNum, count)
    
    ssetting = loadSettings(docFile)
    ssetting["runNum"] += 1
    saveSettings(docFile, ssetting)
      
    if delete:
        deleteOldFile(fromFileSize)        
if __name__ == "__main__":
    mainloop()

    finish(start)