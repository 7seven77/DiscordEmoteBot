import os
from functools import partial

from PIL.Image import NONE

class Directory():
    baseImageDirectory : str = os.path.join('.', 'images')
    
    @staticmethod
    def getImageDirectories() -> list:
        return os.listdir(Directory.baseImageDirectory)

    @staticmethod
    def getImageNames(directoryName : str) -> list:
        path : str = os.path.join(Directory.baseImageDirectory, directoryName)
        if not os.path.isdir(path):
            return None
        return os.listdir(path)

    @staticmethod
    def getImagePath(imagePrefix : str, imageID : str) -> str:
        imageName : str = Directory.matchImage(imagePrefix, f'{imagePrefix}{imageID}.png')
        if imageName == None:
            return None
        path : str = os.path.join(Directory.baseImageDirectory, imagePrefix, imageName)
        return path

    @staticmethod
    def matchImage(imagePrefix : str, imageName : str) -> str:
        options = Directory.getImageNames(imagePrefix)
        areEqual = lambda string1, string2 : string1.capitalize() == string2.capitalize()
        image = list(filter(partial(areEqual, imageName), options))
        if len(image) != 1:
            return None
        return image[0]