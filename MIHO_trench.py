import pyvista as pv

#read image files
texture1 = pv.read_texture("/home/changwan/Pyvista/MIHO_trench/T_221124_W1.jpg")
texture2 = pv.read_texture("/home/changwan/Pyvista/MIHO_trench/T_221124_W2.jpg")
texture3 = pv.read_texture("/home/changwan/Pyvista/MIHO_trench/T_221124_W3.jpg")
texture4 = pv.read_texture("/home/changwan/Pyvista/MIHO_trench/T_221124_W4.jpg")
texture5 = pv.read_texture("/home/changwan/Pyvista/MIHO_trench/T_221124_W5.jpg")
texture6 = pv.read_texture("/home/changwan/Pyvista/MIHO_trench/T_221124_W6.jpg")

#enter info. of the planes
plane1 = pv.Plane(center=(1.0, 0.0, 0.0), direction=(0.0, -1.0, 0.0))
plane2 = pv.Plane(center=(1.0, 1.0, 0.0), direction=(0.0, -1.0, 0.0))
plane3 = pv.Plane(center=(1.0, 2.0, 0.0), direction=(0.0, -1.0, 0.0))
plane4 = pv.Plane(center=(1.0, 3.0, 0.0), direction=(0.0, -1.0, 0.0))
plane5 = pv.Plane(center=(1.0, 4.0, 0.0), direction=(0.0, -1.0, 0.0))
plane6 = pv.Plane(center=(1.0, 5.0, 0.0), direction=(0.0, -1.0, 0.0))

#add the multiple meshes
plotter = pv.Plotter()
plotter.add_mesh(plane6, texture = texture1)
plotter.add_mesh(plane5, texture = texture2)
plotter.add_mesh(plane4, texture = texture3)
plotter.add_mesh(plane3, texture = texture4)
plotter.add_mesh(plane2, texture = texture5)
plotter.add_mesh(plane1, texture = texture6)

#plot
plotter.show_grid()
plotter.show()
#plotter.save('test.vtk')
