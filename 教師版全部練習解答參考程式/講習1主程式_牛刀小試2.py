from visual import *

scene = display(width=800, height=800, background=(0.5,0.5,0)) #設定畫面
x_axis = arrow( axis = vector(1, 0, 0), color=color.white, shaftwidth=0.01)
y_axis = arrow( axis = vector(0, 1, 0), color=color.white, shaftwidth=0.01)
z_axis = arrow( axis = vector(0, 0, 1), color=color.white, shaftwidth=0.01)

A = vector(1, 1, 0)
B = vector(0, 1, 1)

print A+B
arrow(axis= A+B, color = color.red, shaftwidth=0.02)
print A-B
arrow(axis= A-B, color = color.blue, shaftwidth=0.02)
print 5*A
arrow(axis= 5*A, color = color.cyan, shaftwidth=0.02)
print cross(A, B)
arrow(axis=cross(A,B), color = color.green, shaftwidth=0.02)
print dot(A, B)

