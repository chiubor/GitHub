from visual import *
size = 0.1          #球半徑 0.1 m

scene = display(width=800, height=800,  background=(0.5,0.5,0))             	#畫面設定
b1 = sphere(radius = size,  color=color.yellow)         				#畫球1
b2 = sphere(radius = size,  color=color.green)          				#畫球2

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
        v1prime = b1.v - (b1.pos-b2.pos)  * dot (b1.v-b2.v, b1.pos-b2.pos) / abs(b1.pos-b2.pos)**2
        v2prime = b2.v - (b2.pos-b1.pos)  * dot (b2.v-b1.v, b2.pos-b1.pos) / abs(b2.pos-b1.pos)**2
        b1.v, b2.v = v1prime, v2prime
