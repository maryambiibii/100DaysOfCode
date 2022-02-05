import turtle as t
import random
tim = t.Turtle()
screen = t.Screen()
t.colormode(255)

# Challenge 1. Draw a rectangle
for _ in range(4):
    tim.right(90)
    tim.forward(100)
    
   
# Challenge 2. Draw a dotted line
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    
import heroes
print(heroes.gen())


# Challenge 3. Draw different shapes
colors = ["dim gray", "dark green", "tan", "pink", "rosy brown", "medium turquoise", "light blue"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for sides in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(sides)
    
    
# Challenge 4. Random Walk
t.colormode(255)
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rand_color = (r, g, b)
    return rand_color


tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
    
    
# Challenge 5. Draw a Spirograph
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen.exitonclick()
