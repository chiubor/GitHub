from visual import *

scene = display(background = vector(0.5, 0.5, 0))
ball = sphere(radius=0.2, color = color.red)
ceiling = box(length = 1, width = 1, height = 0.02)
ceiling.pos = vector(0, 0, 0)
spring = cylinder(radius = 0.02)
spring.pos = ceiling.pos
ball.pos = 1.0*vector(sin(pi/20), -cos(pi/20), 0)
spring.axis = ball.pos - ceiling.pos
spring.L = abs(spring.axis)
spring.k = 100000
scene.center = vector(0, -spring.L / 2.0, 0)
ball.m = 1

g = vector(0, -9.8, 0)
dt = 0.001
t = 0
ball.v = vector(0, 0, 0)
while True:
    rate(1000)
    t += dt
    spring.axis = ball.pos - ceiling.pos
    F = -spring.k * (abs(spring.axis)-spring.L) * spring.axis.norm()
    a = F/ball.m
    if ball.v.x > 0 and (ball.v + a*dt).x <= 0:
        print t
        t = 0
    ball.v += g*dt + a*dt #- 0.8*ball.v*dt
    ball.pos += ball.v *dt
    
    
