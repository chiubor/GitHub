from visual import *
g=9.8               #重力加速度 9.8 m/s^2
size = 0.25         #球半徑 0.25 m
height = 15.0       #球初始高度 15 m
x2 = 10
y2 = 10

scene = display(width=800, height=800, center = (0,height/2,0), background=(0.5,0.5,0)) #設定畫面
floor = box(length=30, height=0.01, width=10, color=color.blue)             #畫地板

def vcollision(v1, v2, p1, p2):
    v1prime = v1 - (p1-p2)*dot(v1-v2, p1-p2)/abs(p1-p2)**2
    v2prime = v2 - (p2-p1)*dot(v2-v1, p2-p1)/abs(p2-p1)**2
    return v1prime, v2prime

balllist = []
pv_list = [(vector(0, 0, 0), vector(x2, y2, 0)), (vector( x2, y2, 0), vector(0, 0, 0))]        #球初始位置和速度
for (posi,vel) in pv_list:
    balllist.append(sphere(pos=posi, v= vel, radius = size, color=color.red))

dt = 0.001                              #時間間隔 0.001 秒
while balllist[1].pos.y >= size:               #模擬直到球落地 即 y=球半徑
    rate(500)                          #每一秒跑 1000 次

    for ball in balllist:
        ball.pos += ball.v*dt
        ball.v.y += - g*dt
        if ball.v.y < 0 and ball.pos.y <size:
            ball.v.y = -ball.v.y

    if abs(balllist[0].pos - balllist[1].pos)<=2*size and dot(balllist[0].v, balllist[1].v) <= 0 :
        balllist[0].v, balllist[1].v = vcollision(balllist[0].v, balllist[1].v, balllist[0].pos, balllist[1].pos)

        
    
