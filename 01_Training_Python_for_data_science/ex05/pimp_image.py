import numpy as np


def ft_invert(array: np.ndarray):
    """
    Inverts the color of the image received.
    """
    print(255 - array)
    return 255 - array


def ft_red(array: np.ndarray):
    """
    Applies a red filter to the image received.
    """
    red_array = array.copy()
    red_array[:, :, 1] = 0
    red_array[:, :, 2] = 0
    print(red_array)
    return red_array


def ft_green(array: np.ndarray):
    """
    Applies a green filter to the image received.
    """
    green_array = array.copy()
    green_array[:, :, 0] = 0
    green_array[:, :, 2] = 0
    print(green_array)
    return green_array


def ft_blue(array: np.ndarray):
    """
    Applies a blue filter to the image received.
    """
    blue_array = array.copy()
    blue_array[:, :, 0] = 0
    blue_array[:, :, 1] = 0
    print(blue_array)
    return blue_array


def ft_grey(array: np.ndarray):
    """
    Converts the image to grayscale.
    """
    grey_array = array.copy()
    grey_array = (0.2989 * grey_array[:, :, 0] + 0.5870 * grey_array[:, :, 1]
                  + 0.1140 * grey_array[:, :, 2]).astype(np.uint8)
    grey_array = np.stack((grey_array,)*3, axis=-1)
    print(grey_array)
    return grey_array
