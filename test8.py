import pyvista as pv
import numpy as np


points = [[0., 0., 0.],
          [0., 2., 0.],
          [1., 0., 0.],
          [1., 2., 0.]]


face_1 = [4, 0, 1, 2, 3]
face_2 = [4, 4, 5, 6, 7]

faces = np.concatenate((face_1,face_2))

mesh = pv.PolyData(points,faces)
print(mesh)
mesh.plot(show_bounds=True, line_width=5)

