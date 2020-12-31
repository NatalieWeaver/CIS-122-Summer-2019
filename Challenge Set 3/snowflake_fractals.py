'''
Author: Natalie Weaver
Date:   July 17, 2019

CIS 122 Challenge Set 3 just for fun:
Making polygon "snowflake" fractals with recursion

Sources: None
'''

import turtle as t
import math as m
import time

t.screensize(2000, 2000)


def draw_snowflake(n, steps):
    '''
    (int) -> None
    Draws a snowflake of regular polygons with n sides. steps refers to the depth of the fractal.
    For example, steps = 1 would just draw a regular n-gon, steps = 2 would draw a regular n-gon
    with a smaller regular n-gon at each vertex, etc.
    '''

    M = 20 / (1.9 ** n)
    K = n - 2
    N = n

    base_forward = M * n
    step_forward = M * (N ** (2 * steps - 1)) / ((N + K) ** (steps - 1))


    if steps == 1:
        for i in range(n):
            t.forward(base_forward)
            t.left(360.0 / n)
        return None

    for j in range(n):
        t.forward(step_forward)
        t.right(180 - 360.0 / n)
        draw_snowflake(n, steps - 1)
        t.right(180)

    return None


def fractal_animation(highest_n):

    t.hideturtle()
    
    now = time.localtime()

    for n in range(3, highest_n + 1):
        steps = 1
        while steps <= 4:
            M = 20 / (1.9 ** n)
            K = n - 2
            N = n

            side_length = M * (N ** (2 * steps - 1)) / ((N + K) ** (steps - 1))
            
            if time.localtime()[5] != now[5]:
                t.clear()
                t.tracer(0,0)

                t.penup()
                t.goto(-0.5 * side_length, -(side_length / (2 * m.tan(m.pi / n))))
                t.pendown()
                
                draw_snowflake(n, steps)
                t.update()
                steps = steps + 1
                now = time.localtime()

    return None


fractal_animation(9)
t.exitonclick()