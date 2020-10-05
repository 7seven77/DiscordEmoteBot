import os

baseImageDirectory : str = os.path.join('.', 'images')

def getImageDirectories() -> list[str]:
    return os.listdir(baseImageDirectory)

def getImageNames(directoryName : str) -> list[str]:
    path : str = os.path.join(baseImageDirectory, directoryName)
    if not os.path.isdir(path):
        return None
    return os.listdir(path)