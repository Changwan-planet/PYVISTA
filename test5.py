import pyvista as pv


x_axis = pv.Line((0,0,0), (150,0,0))
y_axis = pv.Line((0,0,0), (0,150,0))
z_axis = pv.Line((0,0,0), (0,0,150))


p = pv.Plotter()


p.add_mesh(x_axis,color="red")
p.add_mesh(y_axis,color="blue")
p.add_mesh(z_axis,color="green")



p.show()







