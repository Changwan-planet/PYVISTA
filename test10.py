import pyvista as pv

texture = pv.read_texture("/home/changwan/Pyvista/Mogod_trench/D1_E.jpg")
texture2 = pv.read_texture("/home/changwan/Pyvista/Mogod_trench/D3_E.jpg")

plane1 = pv.Plane(center=(1.0, 0.0, 0.0), 
                  direction=(0.0, 1.0, 0.0))
plane2 = pv.Plane(center=(1.0, 2.0, 0.0), 
                  direction=(0.0, 1.0, 0.0))

plotter = pv.Plotter()
plotter.add_mesh(plane1, texture = texture)
plotter.add_mesh(plane2, texture = texture2)


plotter.show_grid()
plotter.show()

