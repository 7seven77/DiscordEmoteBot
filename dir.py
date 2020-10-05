import os

from PIL.Image import NONE

baseImageDirectory : str = os.path.join('.', 'images')

def getImageDirectories() -> list[str]:
    return os.listdir(baseImageDirectory)

def getImageNames(directoryName : str) -> list[str]:
    path : str = os.path.join(baseImageDirectory, directoryName)
    if not os.path.isdir(path):
        return None
    return os.listdir(path)

def getImagePath(imagePrefix : str, imageName : str) -> str:
    path : str = os.path.join(baseImageDirectory, imagePrefix, f'{imagePrefix}{imageName}.png')
    if os.path.isfile(path):
        return path
    return None