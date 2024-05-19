import os

# Paths
placement = "C:/ProgramData/python"
def try_remove_directory(directory):
    try:
        if os.path.exists(directory):
            with open(directory, "r"):
                for i in directory:
                    os.remove(i) 
            os.rmdir(directory)
            print(f"Directory {directory} removed successfully.")
        else:
            print(f"Directory {directory} does not exist.")
    except PermissionError:
        print(f"Permission denied: Cannot remove directory {directory}.")
    except Exception as e:
        print(f"An error occurred while removing the directory: {e}")




# Try to remove the placement directory
try_remove_directory(placement)
