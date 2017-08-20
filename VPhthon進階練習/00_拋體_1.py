from visual import *

g=9.8		# g = 9.8 m/s^2
size = 0.25	# ball radius = 0.25 m

scene = display(title='ball', center = (0,5,0),width=1000, height=800, background=(0.5,0.5,0))  
floor = box(length=30, height=0.01, width=4, color=color.blue)		# floor
    
dt = 0.001

vlist = [vector(12, 12, 0),
         vector(13, (288-13**2)**.5 , 0),
         vector(11, (288-11**2)**.5, 0)]
ballcolor = [color.red, color.yellow, color.yellow]
for (v, color) in zip(vlist, ballcolor):
    ball = sphere(radius = size,  color=color, make_trail=True)
    ball.pos = vector( -15.0, size, 0.0)	            # ball initial position
    ball.v = v         
                           
    while ball.pos.x < 15 and ball.pos.y >=size : 	

        rate(1000)
        
        ball.v = ball.v + vector(0, - g, 0) * dt 
        ball.pos = ball.pos + ball.v*dt


