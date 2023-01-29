from urllib.request import urlopen
import re
import os
import sys

helpString = '''
gdaria.py is a Python script for downloading large files from Google Drive using aria2

Usage:
  gdaria.py fileid
  gdaria.py help

Options:
  fileid     : Enter the file/folder id from the Google Drive link. For example, if the link is https://drive.google.com/file/d/abc, type in "abc".
  help       : Show this help message.

Example:
  gdaria.py abc

For more information, check the README.md file.
'''


def showDocs(idB=True):
    if idB:
        print("Please enter a file id!")
    print(helpString)


if __name__ == '__main__':
    OUTPUT_DIR = 'downloads'
    if len(sys.argv) > 1:
        if sys.argv[1] == "help":
            showDocs(idB=False)
        elif sys.argv[1] != "":
            with urlopen("https://drive.google.com/uc?export=download&id=" + sys.argv[1]) as res:
                htmlString = res.read().decode()

            dUrl = re.search(
                r'n=\"([^\"]+)', htmlString).group(1).replace('&amp;', '&')

            cmdC = r".\tools\aria2\aria2c " \
                fr"-d {OUTPUT_DIR} " \
                r"-j 5 " \
                r"-x 16 " \
                r"-s 16 " \
                rf'"{dUrl}"'

            print('Input command:', cmdC)
            os.system(cmdC)
        else:
            showDocs()
    else:
        showDocs()
