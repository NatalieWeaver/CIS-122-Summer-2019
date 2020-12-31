'''
Draw a map with exactly four countries such that all four countries are triangles
and each country shares a border with each of the three other countries.
'''

import turtle as t

for i in range(3):
    t.forward(200)
    t.backward(100)
    t.left(120)

t.forward(200)
t.left(180 - 40.898)

for i in range(3):
    t.forward(265)
    t.left(120)
