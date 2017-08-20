from visual import *

size = 0.2
scene = display(center = vector(0, 5, 0), background = vector(0.5, 0.5, 0))
ball1 = sphere(radius = size, color = color.red, make_trail = True)
ball2 = sphere(radius = size, color = color.blue, make_trail = True)
ball3 = sphere(radius = size, color = color.yellow, make_trail = True)
cubec = box(length = 0.32, width = 0.32, height = 0.32, color= color.green, make_trail = True)
ball1.pos = vector(-5, 10, 0)
ball2.pos = vector(-5, 10.5, 0)
ball3.pos = (ball1.pos + ball2.pos)/2.0
cubec.pos = (ball1.pos + ball2.pos)/2.0
floor = box(length=10, width = 10, height = 0.1)



