import turtle
import colorsys

# Set up the screen
s = turtle.Screen()
s.bgcolor("black")

# Create the turtle
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

# Function to draw a circle with a specific color and size
def draw_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw fish body (ellipse approximation)
def draw_fish_body():
    # Draw main body using a stretched circle
    body_color = (255, 165, 0)  # Orange color
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color(body_color)
    t.setheading(0)
    t.pensize(2)
    t.begin_fill()
    for _ in range(2):
        t.circle(100, 90)
        t.circle(50, 90)
    t.end_fill()

# Draw tail
def draw_tail():
    t.penup()
    t.goto(-100, 0)
    t.setheading(150)
    t.pendown()
    t.fillcolor('red')
    t.begin_fill()
    for _ in range(3):
        t.forward(50)
        t.left(120)
    t.end_fill()

# Draw eye
def draw_eye():
    draw_circle('white', 10, 50, 50)
    draw_circle('black', 5, 50, 55)

# Draw the fish
def draw_fish():
    draw_fish_body()
    draw_tail()
    draw_eye()

draw_fish()

# Hide the turtle and display window
t.hideturtle()
turtle.done()

