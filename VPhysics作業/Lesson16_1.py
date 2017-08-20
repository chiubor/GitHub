# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

scene = display(width=1000, height=1000, background=(0.5,0.5,0))
scene.forward = vector(0, -1, 0)

G=6.673E-11

def G_force(mass, pos_vector):
        return -G * sun.mass * mass / mag2(pos_vector) * norm(pos_vector)

sun = sphere(radius = 3.0E10, color = color.orange, material = materials.emissive)
sun.mass = 1.989E30
sun.pos = vector(0,0,0)

earth = sphere(radius = 1.5E10, color= color.blue, material = materials.earth, make_trail = True)
earth.mass = 5.972E24
earth.distance = 1.495E11
earth.v = vector(0,0,2.9783E4)
earth.pos = vector(earth.distance, 0, 0)

#作業：增加一顆火星
#mars.radius = 4.9E9
mars = sphere(radius = 4.9E9, color= color.red, material = materials.marble, make_trail = True)
mars.mass = 6.42E23
mars.distance = 2.279E11
mars.v = vector(0, 0, 2.4077E4)
mars.pos = vector(mars.distance, 0, 0)

#作業：增加一顆哈雷慧星
#halley.radius = 1.0E10
halley = sphere(radius = 1.0E10, color= color.white, material = materials.silver, make_trail = True)
halley.mass = 2.2E14
halley.distance = 8.7665E10
halley.v = vector(0, 0, 54563.3)
halley.pos = vector(halley.distance, 0, 0)

dt = 60*60
while True:
        rate(6*24)

        earth.a = G_force(earth.mass, earth.pos) / earth.mass
        earth.v += earth.a * dt
        earth.pos += earth.v * dt

        mars.a = G_force(mars.mass, mars.pos) / mars.mass
        mars.v += mars.a * dt
        mars.pos += mars.v * dt

        halley.a = G_force(halley.mass, halley.pos) / halley.mass
        halley.v += halley.a * dt
        halley.pos += halley.v * dt

