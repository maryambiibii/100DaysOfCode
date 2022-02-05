
import turtle as t
import random
tur = t.Turtle()
screen = t.Screen()

t.colormode(255)
color_list = [(188, 18, 44), (243, 231, 66), (196, 74, 33), (218, 66, 107), (17, 125, 173), (196, 175, 17), (107, 182, 209), (12, 142, 88), (12, 167, 214), (241, 231, 2), (210, 152, 94), (186, 41, 61), (24, 39, 76), (77, 174, 95), (35, 44, 111), (214, 68, 50), (219, 129, 156), (124, 185, 119), (236, 164, 184), (6, 59, 39), (147, 208, 221), (7, 94, 54), (4, 85, 110), (160, 29, 28), (236, 171, 164), (162, 212, 178), (90, 24, 61), (182, 188, 209), (116, 122, 150), (96, 21, 20)]

tur.penup()
tur.hideturtle()
tur.speed("fastest")

x = -200
y = -200
dots_count = 10
while dots_count:
    tur.goto(x, y)
    for _ in range(10):
        tur.dot(20, random.choice(color_list))
        tur.penup()
        tur.forward(50)
    dots_count -= 1
    y += 50

    
screen.exitonclick()

"""
# To extract colors from an image
import colorgram

colors = colorgram.extract("image.jpg", 2**30)

number_of_colors = []
for i in range(len(colors)):
    color = colors[i]
    rgb_color = color.rgb
    r = rgb_color[0]
    g = rgb_color[1]
    b = rgb_color[2]
    color_rgb_tuple = (r, g, b)
    number_of_colors.append(color_rgb_tuple)

print(number_of_colors)

"""

