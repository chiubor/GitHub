from visual import *
g=9.8               #重力加速度 9.8 m/s^2
size = 0.05         #球半徑 0.05 m
L = 1.0             #細線長 1.0m
m = 0.5             #球重
theta = 20 * pi / 180  #單擺起始角度 = 15 degrees
omega = 0           #初角速度 = 0

scene = display(width=1200, height=1000,center = (0, -L/2, 0), background=(0.5,0.5,0))     #設定畫面
ceiling = box(length=2, height=0.001, width=2, color=color.blue)    #畫天花板
ball = sphere(radius = size,  color=color.red)                      #畫球
string = cylinder(pos=(0,0,0), radius=0.003)                           #畫細線，一端在(0,0,0)
Kbar = box(pos=vector(-1.2, -1.5, 0),length = 0.2, width = 0.2, color = color.cyan)
Vbar = box(pos=vector(-0.9, -1.5, 0), length = 0.2, width = 0.2, color = color.blue)
Ebar = box(pos=vector(-0.6, -1.5, 0), length = 0.2, width = 0.2)


dt = 0.001   
while True:
    rate(1000)

    alpha = -(g/L)*sin(theta)
    omega += alpha * dt
    theta += omega * dt
    
    ball.pos = vector(L * sin(theta), -L*cos(theta), 0)
    string.axis = ball.pos - string.pos
    K =  m*(L*omega)**2/2
    V = m*g*L*(1-cos(theta))

    Kbar.height = K
    Kbar.pos.y =  -1.5 + K/2 
    Vbar.height = V
    Vbar.pos.y =  -1.5 + V/2
    Ebar.height = K+V
    Ebar.pos.y = -1.5 + (K+V)/2

