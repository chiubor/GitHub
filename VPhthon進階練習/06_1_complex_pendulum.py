from visual import *

scene = display(background = vector(0.5, 0.5, 0))
ball1 = sphere(radius=0.05, color = color.red, make_trail = True, retain=50000)
ball2 = sphere(radius=0.05, color = color.blue, make_trail = True, retain=50000)
ceiling = sphere(radius = 0.05)
ceiling.pos = vector(0, 0, 0)
rope1 = cylinder(radius = 0.02)
rope2 = cylinder(radius = 0.02)
rope1.pos = ceiling.pos
ball1.pos = 1.0* vector(sin(pi/6), -cos(pi/6), 0)
ball2.pos = ball1.pos + 0.8*vector(sin(pi), -cos(pi), 0)
rope1.axis = ball1.pos - ceiling.pos
rope1.L = abs(rope1.axis)
rope1.k = 100000
rope2.pos = ball1.pos
rope2.axis = ball2.pos - ball1.pos
rope2.L = abs(rope2.axis)
rope2.k = 100000
scene.center = vector(0, -rope1.L, 0)
ball1.m = 1
ball2.m = 1

g = vector(0, -9.8, 0)
dt = 0.001
t = 0
ball1.v = vector(0, 0, 0)
ball2.v = vector(0, 0, 0)
while True:
    rate(1000)
    t += dt
    rope1.axis = ball1.pos - ceiling.pos
    rope2.pos = ball1.pos
    F1 = -rope1.k * (abs(rope1.axis)-rope1.L) * rope1.axis.norm()
    a1 = F1/ball1.m
    rope2.axis = ball2.pos - ball1.pos
    F2 = -rope2.k * (abs(rope2.axis)-rope2.L) * rope2.axis.norm()
    a2 = F2/ball2.m
    ball1.v += g*dt + a1*dt - a2*dt
    ball1.pos += ball1.v *dt
    ball2.v += g*dt + a2*dt
    ball2.pos += ball2.v *dt
    
    
