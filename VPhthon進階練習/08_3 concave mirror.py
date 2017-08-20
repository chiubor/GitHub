# -*- coding: cp950 -*-
from visual import *
R = 1.0           #球面曲率半徑

scene = display(title="Ray",background=(0.8, 0.8, 0.8), width=700, height=700, center = (0,0,5),fov = 0.04) #設定畫面
circle_board = [(-R * cos(theta), R *sin(theta) ) for theta in arange(-pi/2, pi/2, 0.001)]                  #畫球面鏡
extrusion(pos=[(0,0,-0.5),(0,0,0.5)], shape=circle_board, color=color.yellow)                               #畫球面鏡
cylinder(pos=(-R,0,0),axis=(2*R,0,0), radius = 0.002,color = color.red)                                     #畫光軸

def reflection(normal_vector, in_vector):                               #求反射，條件：法向量，入射向量
    projection = dot(in_vector, normal_vector)*normal_vector            #投影分量=入射向量在法向量方向的投影分量
    trans_vector = in_vector - projection                               #垂直法向量分量=入射向量在垂直法向量方向的分量
    return trans_vector - projection                                    #反射向量=垂直法向量分量-投影分量

dt = 0.003
for d in range(1, 10):
    ray = sphere(color = color.blue, radius = 0.001, make_trail=True)   #畫光線
    ray.pos = vector(-0.6,d*0.06,0)                                     #畫光線開始位置
    ray.v = vector (1.0,0,0)                                            #光線開始時以等速率向正x方向前進

    while ray.pos.y > 0:                                                #處理光線直到光線遇到x軸(即光軸)
        rate(1000)

        ray.pos = ray.pos + ray.v*dt                                    #光線前進
        if abs(ray.pos) >= R and ray.pos.x >0 :                         #遇到球面時
            ray.v = reflection(ray.pos/R,ray.v)                         #光線改以反射向量前進




              
              


