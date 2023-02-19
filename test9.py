import pyvista as pv
import numpy as np

texture2 = pv.read_texture("/home/changwan/Pyvista/Mogod_trench/D3_E.jpg")


#pointa = [0.0, 0.1, 0.0]
#pointb = [0.0, 1.0, 0.0]
#pointc = [1.0, 0.0, 0.0]
#pointd = [1.0, 1.0, 0.0]
#rectangle = pv.Rectangle([pointa, pointb, pointc, pointd])
#rectangle = pv.Rectangle()

#cube = pv.Cube()


#p = pv.Plotter()
#p.add_mesh(rectangle, texture=texture2)
#p.add_mesh(cube, texture=texture2)
#p.show()


plane = pv.Plane()
plane.plot(texture = texture2)
#rectangle.plot(texture = texture2)
