from visual import *
g=9.8/6
size = 0.25		
scene = display(height = 800, width = 800, center = (0,5,0),
                background=(0.5,0.5,0))  
floor = box(length=30, height=0.01, width=4, color=color.blue)		
ball = sphere(radius = size,  color=color.red,
              make_trail=True)


dt = 0.001
ball.pos = vector( -15, size, 0)
ball.v = vector(12, 12, 0)	              
                       
while True: 	
    rate(1000)
    ball.v = ball.v + vector(0, - g, 0) * dt #- 0.9 * ball.v * dt
    ball.pos = ball.pos + ball.v*dt
    if ball.pos.y <= size and ball.v.y <0:
       ball.v.y = -  0.9*ball.v.y
    
    
  

