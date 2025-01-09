from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom_image(image_array: np.ndarray, zoom_factor: float) -> np.ndarray:
    """
    Zoom into the center of the image by a given zoom factor.

    :param image_array: NumPy array of the image.
    :param zoom_factor: Factor by which to zoom into the image.
    :return: Zoomed image as a NumPy array.
    """
    height, width, _ = image_array.shape

    center_x, center_y = width // 2, height // 2

    zoom_width = int(width / zoom_factor)
    zoom_height = int(height / zoom_factor)

    x1 = max(center_x - zoom_width // 2, 0)
    x2 = min(center_x + zoom_width // 2, width)
    y1 = max(center_y - zoom_height // 2, 0)
    y2 = min(center_y + zoom_height // 2, height)

    zoomed_image = image_array[y1:y2, x1:x2]

    return zoomed_image


image_array = ft_load("animal.jpeg")

print(f"The shape of image is: {image_array.shape}")
print(image_array)

zoom_factor = 2
zoomed_image = zoom_image(image_array, zoom_factor)


gray_image = np.dot(zoomed_image[..., :3], 
                    [0.2989, 0.5870, 0.1140]).astype(np.uint8)
print(f"New shape after slicing: {gray_image.shape}")
print(gray_image)

plt.imshow(gray_image, cmap='gray')
plt.axis('on')
plt.show()