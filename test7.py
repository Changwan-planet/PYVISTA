import pyvista


cells = [4, 2, 3, 4, 5]

celltypes = [pyvista.CellType.HEXAHEDRON]

points = [

    [1.0, 1.0, 1.0],

    [1.0, -1.0, -1.0],

    [-1.0, 1.0, -1.0],

    [-1.0, -1.0, 1.0],

]

grid = pyvista.UnstructuredGrid(cells, celltypes, points)

grid.plot(show_edges=True)
"""

points = [[0, 0, 0],
          [1, 0, 0],
          [0.5, 0.667, 0]]
mesh = pyvista.PolyData(points)
mesh.plot(show_bounds=True, cpos='xy', point_size=20)
