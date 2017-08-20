from visual import*
import math

scene1 = display(title="dipole", background=(0.4,0.4,0),autoscale = 0,width=600, height=600,range = 5)

#scene.background = (0.9,0.8,0.4)
pos1 = sphere(display = scene1,pos = (1.0,0,0),color = color.red,radius = 0.1)
neg1 = sphere(display = scene1,pos = (-1.0,0,0),color = color.blue,radius = 0.1)

phi=[-1*pi/2.0+pi*(t+1)/5.0 for t in range(4)]
theta = [2*pi*t/6.0  for t in range(10)]

ch1 = []
t = 0
def E1(x,y,z):
    return 9e9*1e-5/(((x-1.0)**2.0+y**2.0+z**2.0)**1.5)*vector(x-1.0,y,z) - 9e9*1e-5/(((x+1.0)**2.0+y**2.0+z**2.0)**1.5)*vector(x+1.0,y,z) 

for i in range(10):
    for j in range(4):
        ch1.append(sphere(display = scene1,pos = (pos1.pos.x+0.1*sin(phi[j]),pos1.pos.y+0.1*cos(phi[j])*sin(theta[i]),pos1.pos.z+0.1*cos(phi[j])*cos(theta[i])),color = (0.9,1,0.3),radius = 0.015,make_trail = True))

while(1):
    rate(10000)
    t= t +1
    for i in range(40):
        if ((ch1[i].pos.x+1.0)**2+ch1[i].pos.y**2+ch1[i].pos.z**2)>0.01:
            ch1[i].pos = ch1[i].pos +norm(E1(ch1[i].pos.x,ch1[i].pos.y,ch1[i].pos.z))*0.007
    if t>7000:
        break
