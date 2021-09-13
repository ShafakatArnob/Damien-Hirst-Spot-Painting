# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# rgb = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     x = (r, g, b)
#     rgb.append(x)
#
# print(rgb)


import turtle as t
import random

t.colormode(255)
color_list = [(237, 241, 245), (238, 246, 244), (249, 243, 247), (1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]

timmy = t.Turtle()
timmy.speed('fastest')

timmy.penup()
timmy.hideturtle()

timmy.setheading(220)
timmy.forward(300)
timmy.setheading(0)

dots = 100
for i in range(1, dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if i % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = t.Screen()
screen.exitonclick()

