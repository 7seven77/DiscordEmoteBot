import os
import re
from functools import partial

from PIL.Image import NONE

class Directory():
    baseImageDirectory : str = os.path.join('.', 'images')
    
    @staticmethod
    def getImageDirectories() -> list:
        """Get a list of the different directories in the image directory

        Returns
        -------
        list
            The directories in images
        """
        return os.listdir(Directory.baseImageDirectory)

    @staticmethod
    def getImageNames(directoryName : str) -> list:
        """Get the image names from a collection of images

        Parameters
        ----------
        directoryName : str
            Directory from which to get images

        Returns
        -------
        list
            List of images
        """
        path : str = os.path.join(Directory.baseImageDirectory, directoryName)
        if not os.path.isdir(path):
            return None
        return os.listdir(path)

    @staticmethod
    def getImagePath(imagePrefix : str, imageID : str) -> str:
        """Get the path to an image

        Parameters
        ----------
        imagePrefix : str
            The shared beginning of a group of emotes
        imageID : str
            The unique part of the emote name

        Returns
        -------
        str
            Path to the image specified
        """
        imageName : str = Directory.matchImage(imagePrefix, f'{imagePrefix}{imageID}')
        if imageName == None:
            return None
        path : str = os.path.join(Directory.baseImageDirectory, imagePrefix, imageName)
        return path

    @staticmethod
    def matchImage(imageDirectory : str, imageName : str) -> str:
        """Get the name of the image specified 
        Allows a string to be matched to an image regardless of case

        Parameters
        ----------
        imageDirectory : str
            Directory the image is in
        imageName : str
            Full name of the image 

        Returns
        -------
        str
            [description]
        """
        options : list = Directory.getImageNames(imageDirectory)
        if options == None:
            return None
            
        # Matches any string that is the same as the imageName, followed immediately by a '.'
        # Matches are case insensitive and will match any file type
        pattern : re.Pattern = re.compile(f"{imageName}\.\w*", re.IGNORECASE)
        
        areEqual = lambda fileName : pattern.match(fileName) != None
        image = list(filter(areEqual, options))
        # Return None, if there are no matches or more than one
        if len(image) != 1:
            return None
        return image[0]