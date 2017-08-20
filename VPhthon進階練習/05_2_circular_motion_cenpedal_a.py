from visual import *
from visual.graph import *

scene = display(background = vector(0.5, 0.5, 0))
gd = gdisplay(x= 500, background = vector(0.5, 0.5, 0))
FT = gcurve(gdisplay = gd)
ball = sphere(radius=0.2, color = color.red)

rope = cylinder(radius = 0.02)
rope.pos = vector(0, 0, 0)
ball.pos = 1 * vector(1, 0, 0)
rope.axis = ball.pos - rope.pos
rope.L = abs(rope.axis)
rope.k = 1000000
ball.m = 1

dt = 0.001
t = 0
a_all = 0
ball.v = vector(0, 3, 0)
while True:
    rate(1000)
    t += dt
    rope.axis = ball.pos - rope.pos
    F = -rope.k * (abs(rope.axis)-rope.L) * rope.axis.norm()
    a = F/ball.m
    a_all += abs(a)*dt 
    a_average = a_all / t
    FT.plot(pos = (t, a_average))
    ball.v += a*dt
    ball.pos += ball.v *dt
    
    
