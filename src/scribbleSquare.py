import numpy as np
from matplotlib import pyplot as plt
import skimage
from skimage.transform import resize
# import random

# img = skimage.data.load('/Users/stern/Downloads/ScribbleTrace-master/MagrittePipe.jpg', as_gray=True)
basePath = '/Users/stern/Downloads/ScribbleTrace-master/'
fileName = 'MagrittePipe.jpg'
completeName = basePath + fileName
img = skimage.io.imread(completeName, as_gray=True)
# img = skimage.data.camera()
# currently sciplot-image gets used only for reading in the files

output_width = 30.0  # default 20
quantificationlevels = 4  # default 7

randomness_vertex = 0.1  # 0 is no randomness, 0.1 is suitable.
randomness_position = 0.75  # default 0.05

min_pixel_size = 0.1  # deault 0.1
max_pixel_size = 1.1  # default 0.9

small_first = True

scale_factor = round(img.shape[0] / output_width)

img = resize(img, (round(img.shape[0] / scale_factor), round(img.shape[1] / scale_factor)), anti_aliasing=True)
img_orig = img
img = 1 - img
img = np.round(np.multiply(img, quantificationlevels - 1))  # +1


def pixplot():
    pixel_sizes = np.multiply(np.linspace(min_pixel_size, max_pixel_size, quantificationlevels),
                              np.random.uniform(1 - randomness_position, 1 + randomness_position, quantificationlevels))
    if not small_first:
        pixel_sizes = pixel_sizes[::-1]

    pixel_sizes = pixel_sizes[0:val]
    for n in pixel_sizes:
        vert_x = np.array([0, 0, 1, 1])
        vert_y = np.array([0, 1, 1, 0])

        vert_x = vert_x + np.random.uniform(-randomness_vertex, randomness_vertex, 4)
        vert_y = vert_y + np.random.uniform(-randomness_vertex, randomness_vertex, 4)

        vert_x = np.multiply(vert_x - 0.5, n) + c
        vert_y = np.multiply(vert_y - 0.5, n) + r

        vert_x = np.append(vert_x, vert_x[0])
        vert_y = np.append(vert_y, vert_y[0])

        plt.plot(vert_x, vert_y, 'k-')  # plt = pyplot


plt.imshow(img_orig, alpha=0.005, cmap='gray')  # default alpha 0.5

height, width = img.shape
for c in range(width):
    for r in range(height):
        val = np.int(img[r, c])
        pixplot()
# plt.show()
# plt.axis('off')
plt.gcf().patch.set_visible(False)

outName = fileName[:-3] + "svg"
plt.savefig(basePath + outName, bbox_inches="tight")
plt.show()
