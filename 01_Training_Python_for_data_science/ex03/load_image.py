from PIL import Image
import numpy as np


def ft_load(path: str):

    """
    Loads an image and return an array of it, displaying its size, channels
    and pixels in RGB format.

    :param path: The path to the image.jpg/jpeg
    """

    try:
        image = Image.open(path)
        width, height = image.size

        if image.mode != 'RGB':
            image = image.convert('RGB')

        # channels = len(image.getbands())

        # print(f"The shape of image is: ({height}, {width}, {channels})")

        return np.array(image)

    except Exception as e:
        print(f"Error: {e}")
