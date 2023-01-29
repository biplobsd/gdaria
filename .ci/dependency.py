import os
import requests
import sys
from pyunpack import Archive
from urllib.request import urlretrieve
from enum import Enum


class toolType(Enum):
    ARIA2 = 1
    FOUND = 3


def findPackageR(id_repo, p_name, tag_name=False, all_=False):
    for _ in range(5):
        getData = requests.get(f"https://api.github.com/repos/{id_repo}/releases")
        if getData.ok:
            try:
                for rawData in getData.json():
                    if tag_name:
                        if rawData['tag_name'] != tag_name:
                            continue

                    for f in rawData['assets']:
                        if p_name == f['browser_download_url'][-len(p_name):]:
                            rawData['assets'] = f
                            return f['browser_download_url'] if not all_ else rawData
            except:
                continue
            raise Exception(
                f"{id_repo}/{p_name} Not found or maybe api changed!\n Try again with Change packages name")


def isNotAvaCheck():
    if not os.path.exists('tools/aria2/aria2c.exe'):
        print("Aria2 not found")
        return toolType.ARIA2
    else:
        print("All found")
        return toolType.FOUND


def downloadAria2(isx64=True):
    fileName = 'aria2.zip'
    pType = '64' if isx64 else '32'
    doc = findPackageR(
        'aria2/aria2', f'-win-{pType}bit-build1.zip', all_=True
        )['assets']
    pUrl = doc['browser_download_url']
    print(pUrl)
    print('aria2 Downloading...')
    urlretrieve(pUrl,  fileName)
    print('aria2 Downloaded')

    print('aria2 extracting...')
    Archive(fileName).extractall("tools/")
    print('aria2 extracted')

    os.rename('tools/'+doc['name'][:-4], 'tools/aria2')

    os.remove(fileName)

if __name__ == '__main__':
    isx64 = bool(int(sys.argv[1]))

    os.makedirs('tools', exist_ok=True)
    if isNotAvaCheck() == toolType.ARIA2:
        downloadAria2(isx64)
