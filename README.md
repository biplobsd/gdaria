gdaria.py is a Python script for downloading large files from Google Drive using aria2. The script uses the lxml library to parse the HTML from the Google Drive download page, extract the download link, and pass it as an argument to the aria2c command for downloading.

## Installation
No need to install any module dependency, just download gdaria from the release and extract the archive file.

## Usage
To use gdaria.py, you need to run the script in your terminal and pass the file ID as the first argument. For example:

`python gdaria.py abc`

Where "abc" is the file ID, taken from the Google Drive download link: https://drive.google.com/u/0/uc?id=abc&export=download

If you need help, you can run the script with the help argument:
`python gdaria.py help`

## Credits
This script was created by biplobsd and can be found on GitHub at https://github.com/biplobsd/gdaria

## Issues Reporting
To report any issues with the script, please follow these steps:

Go to the GitHub repository of the script: https://github.com/biplobsd/gdaria
1. Click on the "Issues" tab.
2. Click on the "New Issue" button.
3. Provide a clear and descriptive title for the issue.
4. Describe the issue in detail and include any relevant logs or error messages.
5. If possible, include steps to reproduce the issue.
6. Submit the issue.

The developers will look into the issue and try to resolve it as soon as possible.