# -*- coding: cp950 -*-
from visual import *
R = 1.0           #�y�����v�b�|

scene = display(title="Ray",background=(0.8, 0.8, 0.8), width=700, height=700, center = (0,0,5),fov = 0.04) #�]�w�e��
circle_board = [(-R * cos(theta), R *sin(theta) ) for theta in arange(-pi/2, pi/2, 0.001)]                  #�e�y����
extrusion(pos=[(0,0,-0.5),(0,0,0.5)], shape=circle_board, color=color.yellow)                               #�e�y����
cylinder(pos=(-R,0,0),axis=(2*R,0,0), radius = 0.002,color = color.red)                                     #�e���b

def reflection(normal_vector, in_vector):                               #�D�Ϯg�A����G�k�V�q�A�J�g�V�q
    projection = dot(in_vector, normal_vector)*normal_vector            #��v���q=�J�g�V�q�b�k�V�q��V����v���q
    trans_vector = in_vector - projection                               #�����k�V�q���q=�J�g�V�q�b�����k�V�q��V�����q
    return trans_vector - projection                                    #�Ϯg�V�q=�����k�V�q���q-��v���q

dt = 0.003
for d in range(1, 10):
    ray = sphere(color = color.blue, radius = 0.001, make_trail=True)   #�e���u
    ray.pos = vector(-0.6,d*0.06,0)                                     #�e���u�}�l��m
    ray.v = vector (1.0,0,0)                                            #���u�}�l�ɥH���t�v�V��x��V�e�i

    while ray.pos.y > 0:                                                #�B�z���u������u�J��x�b(�Y���b)
        rate(1000)

        ray.pos = ray.pos + ray.v*dt                                    #���u�e�i
        if abs(ray.pos) >= R and ray.pos.x >0 :                         #�J��y����
            ray.v = reflection(ray.pos/R,ray.v)                         #���u��H�Ϯg�V�q�e�i




              
              


