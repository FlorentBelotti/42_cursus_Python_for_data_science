from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


array = ft_load("landscape.jpg")

inverted_array = ft_invert(array)
red_array = ft_red(array)
green_array = ft_green(array)
blue_array = ft_blue(array)
grey_array = ft_grey(array)

print(ft_invert.__doc__)

plt.figure(figsize=(10, 8))

plt.subplot(231)
plt.title("Figure VIII.1: Original")
plt.imshow(array)

plt.subplot(232)
plt.title("Figure VIII.2: Invert")
plt.imshow(inverted_array)

plt.subplot(233)
plt.title("Figure VIII.3: Red")
plt.imshow(red_array)

plt.subplot(234)
plt.title("Figure VIII.4: Green")
plt.imshow(green_array)

plt.subplot(235)
plt.title("Figure VIII.5: Blue")
plt.imshow(blue_array)

plt.subplot(236)
plt.title("Figure VIII.6: Grey")
plt.imshow(grey_array)

plt.show()
