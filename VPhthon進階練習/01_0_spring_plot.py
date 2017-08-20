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

