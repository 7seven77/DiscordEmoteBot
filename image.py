from PIL import Image
import io
import discord

mediumSize : int = (56, 56)
largeSize : int = (112, 112)

def getEmote(path : str) -> discord.File:
    image : Image = Image.open(path)
    image = image.resize(mediumSize)
    with io.BytesIO() as binary:
        image.save(binary, 'PNG')
        binary.seek(0)
        return discord.File(binary, 'image.png')
    