import pyvista 
from pyvista import examples


# Light of the Sun.
light = pyvista.Light()
light.set_direction_angle(30, -20)

# Load planets
mercury = examples.planets.load_mercury(radius=2439.0)
venus = examples.planets.load_venus(radius=6052.0)
earth = examples.planets.load_earth(radius=6378.1)
mars = examples.planets.load_mars(radius=3397.2)
jupiter = examples.planets.load_jupiter(radius=71492.0)
saturn = examples.planets.load_saturn(radius=60268.0)
# Saturn's rings range from 7000.0 km to 80000.0 km from the surface of the planet
inner = 60268.0 + 7000.0
outer = 60268.0 + 80000.0
saturn_rings = examples.planets.load_saturn_rings(inner=inner, outer=outer, c_res=50)
uranus = examples.planets.load_uranus(radius=25559.0)
neptune = examples.planets.load_neptune(radius=24764.0)
pluto = examples.planets.load_pluto(radius=1151.0)

# Move planets to a nice position for the plotter. These numbers are not
# grounded in reality and are for demonstration purposes only.
mercury.translate((0.0, 0.0, 0.0), inplace=True)
venus.translate((-15000.0, 0.0, 0.0), inplace=True)
earth.translate((-30000.0, 0.0, 0.0), inplace=True)
mars.translate((-45000.0, 0.0, 0.0), inplace=True)
jupiter.translate((-150000.0, 0.0, 0.0), inplace=True)
saturn.translate((-400000.0, 0.0, 0.0), inplace=True)
saturn_rings.translate((-400000.0, 0.0, 0.0), inplace=True)
uranus.translate((-600000.0, 0.0, 0.0), inplace=True)
neptune.translate((-700000.0, 0.0, 0.0), inplace=True)

# Add planets to Plotter.
pl = pyvista.Plotter(lighting="none")
cubemap = examples.download_cubemap_space_16k()
_ = pl.add_actor(cubemap.to_skybox())
pl.set_environment_texture(cubemap, True)
pl.add_light(light)
pl.add_mesh(mercury, smooth_shading=True)
pl.add_mesh(venus, smooth_shading=True)
pl.add_mesh(earth, smooth_shading=True)
pl.add_mesh(mars, smooth_shading=True)
pl.add_mesh(jupiter, smooth_shading=True)
pl.add_mesh(saturn, smooth_shading=True)
pl.add_mesh(saturn_rings, smooth_shading=True)
pl.add_mesh(uranus, smooth_shading=True)
pl.add_mesh(neptune, smooth_shading=True)
pl.add_mesh(pluto, smooth_shading=True)
pl.show()
