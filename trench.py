import pyvista as pv
import cv2

import numpy as np
from matplotlib import pyplot as plt



#image = pv.read("/home/changwan/Pyvista/Mogod_trench/D1_E.jpg/")

image = cv2.imread("/home/changwan/Pyvista/Mogod_trench/D1_E.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("/home/changwan/Pyvista/Mogod_trench/D3_E.jpg", cv2.IMREAD_GRAYSCALE)
#image3 = cv2.imread("/home/changwan/Pyvista/Mogod_trench/U2_W.jpg", cv2.IMREAD_GRAYSCALE)
#image4 = cv2.imread("/home/changwan/Pyvista/Mogod_trench/U3_W.jpg", cv2.IMREAD_GRAYSCALE)


print(image.shape)
print(image2.shape)
#print(image3.shape)
#print(image4.shape)

#pyvista
#image.plot(rgb=True, cpos="xy")
#image.plot(cpos="xy")

#opencv
#print(image[0,0])
#image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#plt.imshow(image_rgb), plt.axis("off")
#plt.show()

# Create a cube with dimension 1x1x1
#cube = pv.Cube([5420, 10, 10])
#cube = pv.Cube([5420, 1, 1])
#cube2 = pv.Cube([3222, 1, 1])
#cube = pv.Cube([2, 1, 1])
#cube2 = pv.Cube([2, 1, 1])




# put the cube un a place in space
#cube2.translate([2, 3, 4])

# rotate the cube
#cube.rotate_x(45)

# gives a color for the cube
#cube.color = "red"

# Apply a texture the the cube.
texture = pv.read_texture("/home/changwan/Pyvista/Mogod_trench/D1_E.jpg")
texture2 = pv.read_texture("/home/changwan/Pyvista/Mogod_trench/D3_E.jpg")


p = pv.Plotter()
#p.add_mesh(cube, texture = texture)
p.add_mesh(cube2, texture = texture2)
p.show()
