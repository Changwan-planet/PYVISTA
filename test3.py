import pyvista as pv
from pyvista import examples

mesh = examples.download_carotid()

p = pv.Plotter()
p.add_mesh(mesh.contour(8).extract_largest(), opacity=0.5)


def my_plane_func(normal, origin):
    slc = mesh.slice(normal=normal, origin=origin)
    arrows = slc.glyph(orient='vectors', scale="scalars", factor=0.01)
    p.add_mesh(arrows, name='arrows')


p.add_plane_widget(my_plane_func)
p.show_grid()
p.add_axes()
p.show()
