# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

g = 9.8

scene = display(center=vector(0, -1.0, 0), background=(0.5, 0.5, 0))
ceiling = box(length=1, width=1, height=0.01, color=color.blue)
ball = sphere(radius=0.1, color=color.red, make_trail=True)

ball.pos = vector(1, -1, 0)
ball.m = 0.5
ball.v = vector(0, 0, 0)
# 初始擺盪的繩子
line = cylinder(radius=0.01)
line.pos = ceiling.pos
line.axis = ball.pos - ceiling.pos
line.L = line.length

# 釘子
ratio_length = 0.4  # 釘子與天花板繩子固定點與繩長比例，調整範圍：0 ~ 1
ratio_angle = 0.4  # 釘子與天花板繩子固定點與繩子擺盪範圍最大角度比例，調整範圍：0 ~ 1
angle_limit = 2 * (pi/2 - diff_angle(line.axis, (1, 0, 0)))  # 繩子擺盪範圍最大角度
fixed_point = sphere(radius=0.02, pos=ceiling.pos + ratio_length * ball.pos.rotate(-1 * ratio_angle * angle_limit), color=color.orange)
angle_fixed = diff_angle(fixed_point.pos, (1, 0, 0))  # 釘子向量(由 (0, 0, 0) 起算)和 (1, 0, 0) 的夾角

# 碰到釘子後，擺盪的繩子
line2 = cylinder(radius=0.01)
line2.pos = fixed_point.pos
line2.L = line.L - abs(fixed_point.pos - ceiling.pos)
line2.axis = (0, 0, 0)  # axis 設為 (0, 0, 0) 隱藏
# line2.length = 0  # 也可以

# 正在擺盪的繩子
cline = line

K = 100000.0

dt = 0.001

while True:
    rate(1000)
    # only for 釘子在繩子固定點正下方
    # if ball.pos.x <= fixed_point.pos.x:
    #     line2.axis = ball.pos - fixed_point.pos
    #     line.axis = fixed_point.pos - ceiling.pos
    #     cline = line2
    # else:
    #     line2.length = 0
    #     line.axis = ball.pos - ceiling.pos
    #     cline = line

    # for 釘子在繩子擺盪範圍內
    angle_cline = diff_angle(cline.axis, (1, 0, 0))  # 繩子向量(由 (0, 0, 0) 起算)和 (1, 0, 0) 的夾角
    # angle_fixed = diff_angle(fixed_point.pos, (1, 0, 0))  # 釘子向量(由 (0, 0, 0) 起算)和 (1, 0, 0) 的夾角

    if angle_cline >= angle_fixed:  # 繩子碰到釘子之後
        line2.axis = ball.pos - fixed_point.pos  # 變更 axis，由釘子至球，會出現
        line.axis = fixed_point.pos - ceiling.pos  # 變更 axis，由天花板至釘子
        cline = line2
    else:  # 繩子沒碰到釘子
        line2.axis = (0, 0, 0)  # 隱藏
        # line2.length = 0  # 也可以
        line.axis = ball.pos - ceiling.pos  # 恢復原 axis
        cline = line

    F = - K * (cline.length - cline.L) * cline.axis.norm()
    ball.a = vector(0, -g, 0) + F / ball.m
    ball.v += ball.a * dt
    ball.pos += ball.v * dt
    cline.axis = ball.pos - cline.pos
