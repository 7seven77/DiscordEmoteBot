from PIL import Image

mediumSize : int = (56, 56)
largeSize : int = (112, 112)

def getEmote(path : str):
    image : Image = Image.open(path)
    image = image.resize(mediumSize)
    return image