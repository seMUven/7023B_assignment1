# Name: Yan Ketong
# Assignment One

# ====================
# Task A: Turtle Drawing
# ====================



from turtle import *

def task_a_turtle_drawing():
    speed(10)
    bgcolor("black")
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta"]
    pensize(2)

    # ========== 图形1：彩色螺旋正方形（左侧） ==========
    penup()
    goto(-180, 0)   # 移到左边
    pendown()
    for i in range(60):
        color(colors[i % len(colors)])
        for j in range(4):
            forward(60 + i * 2)
            left(90)
        left(7)

    # ========== 图形2：彩色五角星（右侧） ==========
    penup()
    goto(150, 50)   # 移到右边
    pendown()
    right(60)       # 调整一下朝向
    for i in range(36):
        color(colors[i % len(colors)])
        begin_fill()
        for j in range(5):
            forward(100)
            right(144)
        end_fill()
        right(10)

    # 画完保持窗口，不自动关闭
    done()

# 执行
task_a_turtle_drawing()
