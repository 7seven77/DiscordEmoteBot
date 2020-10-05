import os
from os import stat

from PIL.Image import NONE

class Directory():
    baseImageDirectory : str = os.path.join('.', 'images')
    
    @staticmethod
    def getImageDirectories() -> list[str]:
        return os.listdir(Directory.baseImageDirectory)

    @staticmethod
    def getImageNames(directoryName : str) -> list[str]:
        path : str = os.path.join(Directory.baseImageDirectory, directoryName)
        if not os.path.isdir(path):
            return None
        return os.listdir(path)

    @staticmethod
    def getImagePath(imagePrefix : str, imageName : str) -> str:
        path : str = os.path.join(Directory.baseImageDirectory, imagePrefix, f'{imagePrefix}{imageName}.png')
        if os.path.isfile(path):
            return path
        return None