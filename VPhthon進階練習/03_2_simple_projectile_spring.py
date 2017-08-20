from visual import *

size = 0.2
scene = display(center = vector(0, 4, 0), background = vector(0.5, 0.5, 0))
ball1 = sphere(radius = size, color = color.red, make_trail = True)
ball2 = sphere(radius = size, color = color.blue, make_trail = True)
ball3 = sphere(radius = size, color = color.yellow, make_trail = True)
cubec = box(length = 0.32, width = 0.32, height = 0.32, color= color.green, make_trail = True)
ball1.pos = vector(-5, size, 0)
ball2.pos = vector(-6, size, 0)
ball3.pos = (ball1.pos + ball2.pos)/2.0
cubec.pos = (ball1.pos + ball2.pos)/2.0
floor = box(length=12, width = 10, height = 0.1)

spring = helix(radius = 0.1, coils = 10, thickness = 0.05)
spring.pos = ball1.pos
spring.axis = ball2.pos - ball1.pos
spring.L = abs(spring.axis)
spring.k = 100000

ball1.m = 1
ball2.m = 1
all_ball = [ball1, ball2, ball3]
dt = 0.001
g = vector(0, -9.8, 0)
ball1.v = vector(4, 12, 0)
ball2.v = vector(10, 4, 0)
ball3.v = vector(7, 8, 0)
while ball3.y>=size:
    rate(500)
    ball3.v = ball3.v + g*dt 
    ball3.pos = ball3.pos + ball3.v*dt
    
while ball1.y >= size and ball2.y >= size :
    rate(100)
    spring.pos = ball1.pos
    spring.axis = ball2.pos - ball1.pos
    F = - spring.k * (abs(spring.axis)-spring.L) * spring.axis.norm()
    ball1.v = ball1.v + g*dt - F / ball1.m * dt
    ball1.pos = ball1.pos + ball1.v*dt
    ball2.v = ball2.v + g*dt + F / ball1.m * dt
    ball2.pos = ball2.pos + ball2.v*dt

    cubec.pos = (ball1.pos + ball2.pos)/2.0




