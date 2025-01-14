from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def cut_square(image_array: np.ndarray) -> np.ndarray:
    """
    Cut a square part from the center of the image.

    :param image_array: NumPy array of the image.
    :return: Square part of the image as a NumPy array.
    """
    height, width, _ = image_array.shape
    min_dim = min(height, width)

    center_x, center_y = width // 2, height // 2

    x1 = center_x - min_dim // 4
    x2 = center_x + min_dim // 4
    y1 = center_y - min_dim // 4
    y2 = center_y + min_dim // 4

    square_image = image_array[y1:y2, x1:x2]

    return square_image


image_array = ft_load("animal.jpeg")

if image_array is not None:
    print(f"The shape of image is: {image_array.shape}")
    print(image_array)

    square_image = cut_square(image_array)

    square_image_pil = Image.fromarray(square_image)

    gray_image = square_image_pil.convert('L')

    min_dim = min(gray_image.size)
    gray_image = gray_image.resize((min_dim, min_dim))

    rotated_image = gray_image.rotate(90)

    rotated_image_array = np.array(rotated_image)

    print(f"The shape of rotated image is: {rotated_image_array.shape}")
    print(rotated_image_array)

    plt.imshow(rotated_image_array, cmap='gray')
    plt.axis('on')
    plt.show()
else:
    print("Failed to load image.")
