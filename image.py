from PIL import Image
import io
import discord
import os

mediumSize : int = (56, 56)
largeSize : int = (112, 112)
 
def getEmoteFromFiles(path : str) -> discord.File:
    """Open and resize a file ready to be sent to Discord

    Parameters
    ----------
    path : str
        Where the image is located

    Returns
    -------
    discord.File
        The image ready to be sent
    """
    type : str = os.path.splitext(path)[1][1:].upper()
    if type == "GIF":
        return discord.File(path)

    # Open and resize the image
    image : Image = Image.open(path)
    image = image.resize(mediumSize)
    # Convert the image to bytes then into a Discord.File
    with io.BytesIO() as binary:
        image.save(binary, type)
        binary.seek(0)
        fileName : str = os.path.basename(path)
        return discord.File(binary, fileName)
    