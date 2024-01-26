# Google Drive Large File Downloader

## Description
This script facilitates the downloading of large files from Google Drive on Linux systems. It generates a curl command and copies it to the clipboard, making it easy to start the download from the terminal.

## Installation
Clone this repository or download the script directly. Make sure Python is installed on your system.

## Requirements
- Python
- Pyperclip (`pip install pyperclip`)

## Usage

This script is designed to be run from the command line. It takes two arguments: the ID of the Google Drive file you want to download and the desired name for the output file.

### Steps to Use:
1. **Run the Script**: Open your terminal and navigate to the directory containing the script. Use the following command format:

    ```bash
    python gdrive_cmd_gen.py <file_id> <output_filename>
    ```

    Replace `<file_id>` with the actual ID of the Google Drive file and `<output_filename>` with the name you want the downloaded file to have.

2. **Get the Download Command**: After running the script, the appropriate download command is copied to your clipboard.

3. **Download the File**: Simply paste the command in your terminal to start the download process.

### Example

Suppose you want to download a file from Google Drive with the ID `1a2b3c4d5e6f` and you want to save it as `downloaded_file.zip`. You would run the following command:

```bash
python gdrive_cmd_gen.py 1a2b3c4d5e6f downloaded_file.zip
