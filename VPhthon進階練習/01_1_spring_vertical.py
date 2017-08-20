from visual import *

scene = display(background = vector(0.5, 0.5, 0))
ball = sphere(radius=0.2, color = color.red)
ceiling = box(length = 1, width = 1, height = 0.02)
ceiling.pos = vector(0, 0.5, 0)
spring = helix(radius = 0.1, coils = 10, thickness = 0.02)
spring.pos = ceiling.pos
spring.axis = ball.pos - ceiling.pos
spring.L = abs(spring.axis)
spring.k = 10
ball.m = 1
g = vector(0, -9.8, 0)
dt = 0.001
t = 0
ball.v = vector(0, 0, 0)
while True:
    rate(1000)
    t = t + dt
    spring.axis = ball.pos - ceiling.pos
    F = -spring.k * (abs(spring.axis)-spring.L) * spring.axis.norm()
    a = F/ball.m
    if ball.v.y > 0 and (ball.v + g*dt + a*dt).y <=0:
        print t
        t = 0
    ball.v += g*dt + a*dt #- 0.5*ball.v*dt
    ball.pos += ball.v *dt











    
