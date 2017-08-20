from visual import *

scene1 = display(width=600, center = (0, -0.3, 0),
                 height=400, background=(0.5,0.5,0))
ceiling = box(length = 1, width = 1, height = 0.01)

all_ball = []
all_rope = []
for i in range(5):
    all_ball.append(sphere(pos = (i*0.2-0.4, -0.5, 0), radius=0.1)) 
    all_rope.append(cylinder(pos = (i*0.2-0.4, 0, 0),  radius = 0.01, color= color.red))

for i in range(5):
    all_rope[i].axis = all_ball[i].pos - all_rope[i].pos
    all_rope[i].L = abs(all_rope[i].axis)
    all_ball[i].v = vector(0,0,0)

all_ball[4].pos = all_rope[4].pos + all_rope[4].L * vector(sin(pi/6), -cos(pi/6), 0)
all_ball[3].pos = all_rope[3].pos + all_rope[3].L * vector(sin(pi/6), -cos(pi/6), 0)
all_ball[2].pos = all_rope[2].pos + all_rope[2].L * vector(sin(pi/6), -cos(pi/6), 0)
all_ball[1].pos = all_rope[1].pos + all_rope[1].L * vector(-sin(pi/6), -cos(pi/6), 0)
all_ball[0].pos = all_rope[0].pos + all_rope[0].L * vector(-sin(pi/6), -cos(pi/6), 0)

k = 100000
m = 0.5
g = vector(0, -9.8, 0)
    
def collide(v1,v2,m1,m2):
    v1f = v1*(m1-m2)/(m1+m2) + v2*2*m2/(m1+m2)
    v2f = v1*2*m1/(m2+m1) + v2*(m2-m1)/(m2+m1)
    return v1f, v2f

dt = 0.0001
t = 0
while True:
    rate(3000)
    t += dt

    for i in range(5):
        all_rope[i].axis = all_ball[i].pos - all_rope[i].pos
        F = -k*(abs(all_rope[i].axis)-all_rope[i].L) * all_rope[i].axis.norm()
        a = F/m
        all_ball[i].v += g*dt + a*dt
        all_ball[i].pos += all_ball[i].v *dt

        if i < 4:
            if ( abs(all_ball[i].pos-all_ball[i+1].pos) <
                 (all_ball[i].radius+all_ball[i+1].radius) and
                 all_ball[i].v.x > all_ball[i+1].v.x):
                all_ball[i].v, all_ball[i+1].v = collide(all_ball[i].v,all_ball[i+1].v, m, m)
    
    
