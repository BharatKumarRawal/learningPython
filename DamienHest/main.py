import colorgram
import random
import turtle
import turtle as turtle_module
turtle_module.colormode(255)
tim = turtle_module.Turtle()

colors = colorgram.extract("imags.jpg", 10)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100
tim.speed(0)
colors_list = [(109, 178, 213), (218, 127, 174), (166, 54, 95), (206, 80, 126), (154, 18, 51), (32, 108, 158), (193, 209, 224), (240, 158, 206), (138, 99, 40), (62, 18, 38)]
for dot_count in range(1, number_of_dots + 1):
    tim.dot(15, random.choice(colors_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()
