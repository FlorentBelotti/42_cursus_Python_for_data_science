from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image and returns an array of it, displaying its size, channels
    and pixels in RGB format.

    :param path: The path to the image.jpg/jpeg
    :return: NumPy array of the image.
    """
    try:
        image = Image.open(path)
        width, height = image.size

        if image.mode != 'RGB':
            image = image.convert('RGB')

        image_array = np.array(image)
        channels = image_array.shape[2]
        print(f"The shape of image is: ({height}, {width}, {channels})")

        return image_array

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
