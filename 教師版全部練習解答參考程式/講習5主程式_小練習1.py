from visual import *
size = 0.1          #球半徑 0.1 m

scene = display(width=800, height=800,  background=(0.5,0.5,0))             	#畫面設定
b1 = sphere(radius = size,  color=color.yellow)         				#畫球1
b2 = sphere(radius = size,  color=color.green)          				#畫球2

def vcollision(v1, v2, p1, p2):
    v1prime = v1 - (p1-p2)*dot(v1-v2, p1-p2)/abs(p1-p2)**2
    v2prime = v2 - (p2-p1)*dot(v2-v1, p2-p1)/abs(p2-p1)**2
    return v1prime, v2prime

b1.pos = vector( 0.6 , 0.1, 0)                        	#球1初位置
b2.pos = vector( 0 , 0 , 0)                           	#球2初位置
b1.v = vector(-0.2, 0, 0)                              	#球1初速
b2.v = vector(0 , 0, 0)                                	#球2初速

dt = 0.001                                                          
while True:
    rate(1000)
					
    b1.pos += b1.v * dt 
    b2.pos += b2.v * dt

    if abs(b1.pos - b2.pos)<=2*size and dot(b1.v, b2.v) <= 0 :
        b1.v, b2.v = vcollision(b1.v, b2.v, b1.pos, b2.pos)
