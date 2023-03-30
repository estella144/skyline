import logging
import turtle

SKY_COLOR = "#00d0ff"
BUILDING_1_COLOR = "#7d8e91"
BUILDING_2_COLOR = "#aa4a44"
DOOR_COLOR = "#ffffff"
WINDOW_COLOR = "#00d0ff"

logging_level = logging.DEBUG

def draw_eq_tri(turtle, side_length, start_heading, start_x, start_y, color, fill):
    turtle.seth(start_heading)
    turtle.pu()
    turtle.goto(start_x, start_y)
    turtle.pd()

    turtle.color(color)

    if fill:
        turtle.begin_fill()

    for i in range(3):
        turtle.forward(side_length)
        turtle.right(60)

    turtle.end_fill()

def draw_rect(turtle, length, width, start_x, start_y, color, fill):
    """Draws a rectangle.
Note: turtle will end with heading 90 (north)"""

    logging.debug(f"draw_rect called with arguments turtle={turtle}, length={length}, width={width}, start_x={start_x}, start_y={start_y}, color={color}, fill={fill}")
    turtle.pu()
    turtle.goto(start_x, start_y)
    turtle.pd()
    
    turtle.seth(90)
    turtle.color(color)
    
    if fill:
        turtle.begin_fill()
    
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)

    turtle.end_fill()

def draw_window(turtle, height, start_x, start_y, color):
    
    turtle.seth(90)
    draw_rect(turtle, height, height, start_x, start_y, color, True)
    draw_rect(turtle, height, height, start_x, start_y, "black", False)
    turtle.forward(height/2)
    turtle.right(90)
    turtle.forward(height)
    for i in range(2):
        turtle.left(90)
        turtle.forward(height/2)
    turtle.left(90)
    turtle.forward(height)

def draw_bg(turtle):
    """Draws a frame for a picture."""

    draw_rect(turtle, 400, 400, -200, -200, SKY_COLOR, True)

def draw_building_1(turtle):

    draw_rect(turtle, 400, 400/5, -40, -200, BUILDING_1_COLOR, True)

def draw_building_2(turtle, start_x, start_y):

    draw_rect(turtle, 300, 400/5, start_x, start_y, DOOR_COLOR, True)

def draw_house(turtle, start_x, start_y, i):

    draw_rect(turtle, 100, 400/4, start_x, start_y, BUILDING_2_COLOR, True)
    if i != 200:
        draw_eq_tri(turtle, 100, 60, start_x, start_y + 100, BUILDING_2_COLOR, True)
    draw_rect(turtle, 30, 15, start_x+80/13+30/2, start_y, DOOR_COLOR, True)
    draw_window(turtle, 30, start_x+30+80/3, start_y+40/3, WINDOW_COLOR)
    draw_window(turtle, 30, start_x+30+80/3, start_y+40+40/3, WINDOW_COLOR)
    draw_window(turtle, 30, start_x+80/3, start_y+40+40/3, WINDOW_COLOR)
    
def draw_layer_2(turtle):

    draw_building_2(turtle, -140, -200)
    draw_building_2(turtle, 60, -200)

def draw_layer_3(turtle):
    
    for i in range(-200, 300, 100):
        draw_house(turtle, i, -200, i)

def draw_picture(turtle):
    
    draw_bg(turtle)
    draw_building_1(turtle)
    draw_layer_2(turtle)
    draw_layer_3(turtle)
    
t = turtle.Turtle()
t.speed(20)
draw_picture(t)
