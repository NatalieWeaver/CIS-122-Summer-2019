'''
Author: Natalie Weaver
Date:   July 17, 2019

CIS 122 Challenge Set 3 Part 2: Recursive tree with turtle

Sources: None
'''

import turtle as t

def col_num(n):
    if n % 6 == 1:
        return "red"
    elif n % 6 == 2:
        return "orange"
    elif n % 6 == 3:
        return "yellow"
    elif n % 6 == 4:
        return "green"
    elif n % 6 == 5:
        return "blue"
    else:
        return "purple"


def draw_tree(steps, angle, colors):
    '''
    (int, float, boolean) -> None
    Draws a tree by recursion, with given number of steps.
    At each step, two branches diverge with the given angle between them.
    If colors is True, draw the tree in a different color at each step.
    Otherwise, draw the whole thing in black.
    '''

    ang = (180 - (angle % 360)) / 2

    if steps == 1:
        t.right(ang)

        t.pendown()
        if colors:
            t.pencolor(col_num(steps))
        else:
            t.pencolor("black")
        t.forward(10)
        t.penup()
        
        t.backward(10)
        t.right(180 - 2 * ang)
        
        t.pendown()
        if colors:
            t.pencolor(col_num(steps))
        else:
            t.pencolor("black")
        t.forward(10)
        t.penup()
        
        t.backward(10)

        return None

    t.right(ang)

    t.pendown()
    if colors:
        t.pencolor(col_num(steps))
    else:
        t.pencolor("black")
    t.forward(5 * 2**steps)
    t.penup()
    
    t.setheading(0)
    draw_tree(steps - 1, angle, colors)
    t.left(180 - 2 * ang)
    t.backward(5 * 2**steps)

    t.right(180 - 2 * ang)

    t.pendown()
    if colors:
        t.pencolor(col_num(steps))
    else:
        t.pencolor("black")
    t.forward(5 * 2**steps)
    t.penup()
    
    t.setheading(0)
    draw_tree(steps - 1, angle, colors)
    t.backward(5 * 2**steps)

    return None

t.speed(0)
t.hideturtle()

draw_tree(5, 45, True)

t.exitonclick()