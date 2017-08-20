# 2015/6/22 by MFShih
from visual import *
from vphysics import *

g = 9.8
N, k = 50, 60.0
m, d, thickness = 0.007, 0.022, 0.005
damping, ratio, last_ball_r = 1.5, 3.0, 4*d
ball, s, release = [], [], 0
dt = 0.001

def startfall(evt):
    global release, dt, damping
    dt, damping, release = 0.0002, 0, 1
    return

scene = display(title='slinky', width=400, height=700, center = (0, d*N/0.7,0), forward = (-0.4, 0, -0.6), background=(0.5,0.5,0))
floor = box(length = 0.5, height = 0.0001, width = 0.5, color = color.blue, pos = (0, 0, 0) )
aruler = ruler(pos=(-0.3 , 0, 0), axis=(0,1,0), unit = 0.2, length = 3.0)
label(pos=(0, 3.23, 0), box =False, text= 'Click to release upper end of spring\n and observe in 1/5 slow motion')
scene.bind('click', startfall)

for i in range(N):
    ball.append(sphere(pos=(0,3.0-d * i,0), radius = 0, color = color.red))
    ball[i].v = 0
    if i == N-1 : break
    s.append(helix(coils = 1, pos=(0, ball[i].pos.y, 0), axis=(0,-d,0), radius=4*d, thickness = 2*thickness))
    s[i].s = d
ball[N-1].radius = last_ball_r

while True :  
    rate(1000)

    for i in range(N):                                                                                  #calculate the acceleration of each section
        if i==0 : a = - g - k*(s[i].s-d) / m if release else 0
        elif i==N-1 : a = k*(s[i-1].s-d) / (2* m) - (ratio+1)*g - damping * ball[i].v
        else: a = k*(s[i-1].s-d)/ m - k*(s[i].s-d) / m - g - damping * ball[i].v
        ball[i].v= ball[i].v + a * dt                                                       # equation of motion of each spring section
        ball[i].pos.y = ball[i].pos.y + ball[i].v * dt       
        if i!=0 and ball[i].pos.y >= ball[i-1].pos.y - thickness and (ball[i].v - ball[i-1].v) > 0 :     #spring section hit neighbor section
            ball[i].v, ball[i-1].v = (ball[i].v + ball[i-1].v)/2, (ball[i].v + ball[i-1].v)/2
            ball[i-1].pos.y = ball[i].pos.y + thickness
    if (ball[N-1].pos.y < last_ball_r ) and (ball[N-1].v <0):     #last ball hit the ground
        ball[N-1].pos.y, ball[N-1].v = last_ball_r, - ball[N-1].v
    for i in range(N-1):                                                                    # draw spring sections                                                                   
        s[i].s = ball[i].pos.y - ball[i+1].pos.y
        s[i].pos.y = ball[i].pos.y
        s[i].axis =(0,-s[i].s,0)


        



