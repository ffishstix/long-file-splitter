# File Splitter

This Python script allows you to split a large text file into smaller chunks and save them in a specified location. The script prompts the user for input regarding the file to be split, the destination folder for the split files, and the desired size of each chunk.

## Features

- **User Prompts**: Guides the user through providing the necessary inputs.
- **File Size Calculation**: Automatically determines the size of the file to be split.
- **Custom Chunk Size**: Allows the user to specify the size of the smaller chunks.
- **Randomized Filenames**: Generates unique filenames for the split files to prevent overwriting.
- **Directory Management**: Checks for the existence of the specified directory and creates it if necessary.

## Requirements

- Python 3.x
- Standard Python libraries (`os`, `time`, `string`, `random`, `pathlib`)

## Usage

1. **Run the Script**: Execute the script in a Python environment.
   ```bash
   python file_splitter.py

### Installing Python

Ensure you have Python 3.x installed. If you don't have it or need to update, follow the steps below.

#### Download Python:

1. Go to the [official Python website](https://www.python.org/downloads/).
2. Download the latest Python 3.x installer for your operating system.

#### Install Python:

- **Windows**:
  1. Run the installer.
  2. Make sure to check the box that says "Add Python to PATH".
  3. Follow the prompts to complete the installation.
- **macOS**:
  1. Open the downloaded `.pkg` file.
  2. Follow the prompts to complete the installation.
- **Linux**:
  1. Use a package manager to install Python. For example, on Ubuntu:
     ```bash
     sudo apt update
     sudo apt install python3
     ```
