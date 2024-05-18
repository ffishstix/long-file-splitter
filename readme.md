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
