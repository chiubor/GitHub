from visual import *

scene = display(background = vector(0.5, 0.5, 0))
ball = sphere(radius=0.2, color = color.red)

rope = cylinder(radius = 0.02)
rope.pos = vector(0, 0, 0)
ball.pos = vector(1, 0, 0)
rope.axis = ball.pos - rope.pos
rope.L = abs(rope.axis)
rope.k = 100000
ball.m = 1

dt = 0.001
t = 0
ball.v = vector(0, 3, 0)
while True:
    rate(1000)
    t += dt
    rope.axis = ball.pos - rope.pos
    F = -rope.k * (abs(rope.axis)-rope.L) * rope.axis.norm()
    a = F/ball.m
    if ball.v.x >0 and ball.v.x + a.x*dt <=0:
        print t
        t = 0
    ball.v += a*dt
    ball.pos += ball.v *dt
    
    
