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
k = 0.05

g = vector(0, -9.8, 0)
dt = 0.001
t = 0
cube.v = vector(2, 0, 0)
while True:
    rate(1000)
    spring.axis = cube.pos - wall.pos
    F = -spring.k * (abs(spring.axis)-spring.L) * spring.axis.norm()
    a = F/cube.m - 9.8*cube.m*k*cube.v.norm()/cube.m
    cube.v += a*dt
    cube.pos += cube.v *dt






    


