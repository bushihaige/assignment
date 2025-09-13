import turtle
import colorsys

# Set up the screen
s = turtle.Screen()
s.bgcolor("black")

# Create the turtle
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

# Function to draw a petal
def draw_petal(color, radius, angle):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.end_fill()

# Draw a flower with petals
num_petals = 36
h = 0  # hue start
n = num_petals  # total number of petals

for i in range(num_petals):
    # Generate color for each petal
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color = tuple(int(255 * x) for x in c)
    t.color(color)
    
    # Position turtle for each petal
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(i * (360 / num_petals))
    
    # Draw a petal
    draw_petal(color, radius=100, angle=60)
    
    h += 1 / n  # Increment hue for color variation

# Hide the turtle and display the window
t.hideturtle()
turtle.done()

