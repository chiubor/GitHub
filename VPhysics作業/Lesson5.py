# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

#畫布
scene = display(center=(0.2, 0.5, 0.5), width=600, height=600, background=(0.5,0.6,0.5))

# x軸箭頭
x_axis = arrow(axis=(1, 0, 0), shaftwidth=0.01)
# y軸箭頭
y_axis = arrow(axis=(0, 1, 0), shaftwidth=0.01)
# z軸箭頭
z_axis = arrow(axis=(0, 0, 1), shaftwidth=0.01)

# x軸標籤
label(pos=(1.1,0,0), text='x', box=False)
# y軸標籤
label(pos=(0,1.1,0), text='y', box=False)
# z軸標籤
label(pos=(0,0,1.1), text='z', box=False)

#畫出二個向量
vector1 = vector(1.5, 0.5, 0)
arrow(axis=vector1, color=color.black, shaftwidth=0.02)
vector2 = vector(-1, 1, 0)
arrow(axis=vector2, color=color.black, shaftwidth=0.02)

#向量加法運算
final_vector = vector1 + vector2
arrow(axis=final_vector, color=color.red, shaftwidth=0.02)

# vector1座標標籤
label(pos=vector1, text=str(vector1), opacity=0, box=False)
# vector2座標標籤
label(pos=vector2, text=str(vector2), opacity=0, box=False)
# final_vector座標標籤
label(pos=final_vector, text=str(final_vector), opacity=0, box=False)
