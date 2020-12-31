'''
Author: Natalie Weaver
Date:   July 17, 2019

CIS 122 Challenge Set 3 Part 1: Turtle clock

Sources: None
'''

import turtle as t
import time

t.screensize(500, 500)

hands = t.Turtle()
dig = t.Turtle()


# First, draw the clock face.

def draw_analogue():
    '''
    () -> None
    Draws the face of the clock (not the hands)
    '''

    t.pensize(3)

    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.circle(200)

    t.penup()
    t.goto(0, -10)
    t.setheading(90)

    for i in range(1, 13):
        t.right(30 * i)
        t.forward(175)
        t.write(str(i), align = "center" , font = ("Arial" , 20 , "normal"))
        t.goto(0, -10)
        t.setheading(90)

    t.hideturtle()
    
    return None

def draw_hands():
    '''
    () -> None
    Draws the hour, minute, and second hands to display the time at which the program is run.
    '''

    # hour hand
    hands.home()
    hands.setheading(90)
    hands.pendown()
    hands.pensize(5)
    hands.right(30 * (time.localtime()[3] % 12))
    hands.right(0.5 * time.localtime()[4])
    hands.forward(100)
    hands.penup()

    # minute hand
    hands.home()
    hands.setheading(90)
    hands.pendown()
    hands.right(6 * time.localtime()[4])
    hands.forward(150)
    hands.penup()

    # second hand
    hands.home()
    hands.setheading(90)
    hands.pencolor("red")
    hands.pendown()
    hands.right(6 * time.localtime()[5])
    hands.forward(150)
    hands.penup()
    hands.pencolor("black")
    hands.hideturtle()

    return None

def draw_digital():
    '''
    () -> None
    Draws the digial clock frame (does not display the time)
    '''

    t.goto(-160, -300)
    t.setheading(0)
    t.pendown()
    
    for i in range(4):
        if i % 2 == 0:
            t.forward(320)
        else:
            t.forward(70)
        t.left(90)

    t.penup()
    
    t.goto(-120, -290)
    t.write("hours", align = "center" , font = ("Arial" , 12 , "normal"))

    t.goto(-40, -290)
    t.write("minutes", align = "center" , font = ("Arial" , 12 , "normal"))

    t.goto(40, -290)
    t.write("seconds", align = "center" , font = ("Arial" , 12 , "normal"))

    return None

def digital_time():
    '''
    () -> None
    Displays the time on the digial clock.
    '''
    
    dig.penup()
    
    dig.goto(-120, -275)
    dig.write(str(time.localtime()[3] % 12) , align = "center" , font = ("Arial" , 24 , "normal"))

    dig.goto(-40, -275)
    dig.write(str(time.localtime()[4]) , align = "center" , font = ("Arial" , 24 , "normal"))

    dig.goto(40, -275)
    dig.write(str(time.localtime()[5]) , align = "center" , font = ("Arial" , 24 , "normal"))

    dig.goto(120, -275)
    if time.localtime()[3] < 12:
        dig.write("AM", align = "center" , font = ("Arial" , 24 , "normal"))
    else:
        dig.write("PM", align = "center" , font = ("Arial" , 24 , "normal"))

    dig.hideturtle()
        
    return None


print(time.localtime())

t.speed(0)
#t.tracer(0,0)
draw_analogue()
draw_digital()
t.update()

now = time.localtime()
forever = 1
while forever:
    if time.localtime()[3:6] != now[3:6]:
        hands.clear()
        draw_hands()

        dig.clear()
        digital_time()
        
        t.update()
       


    
print(time.localtime())
