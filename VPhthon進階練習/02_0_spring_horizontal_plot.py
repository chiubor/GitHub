from visual import *

scene = display(center = vector(1, 0, 0), background = vector(0.5, 0.5, 0))
cube = box(length = 0.2, width = 0.2, height= 0.2, color = color.red)
wall = box(length = 0.01, width = 0.5, height = cube.height)
wall.pos = vector(0, wall.height/2.0, 0)
floor = box(length = 2, width = 0.5, height = 0.02)
floor.pos = vector(floor.length / 2, 0, 0)
spring = helix(radius = 0.08, coils = 10, thickness = 0.02)
spring.pos = wall.pos
cube.pos = vector(1, cube.height/2, 0)
spring.axis = cube.pos - wall.pos
spring.L = abs(spring.axis)
spring.k = 10
cube.m = 1



