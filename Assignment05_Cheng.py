# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 21:43:28 2025

@author: madel
"""
# Right-Angled Triangle
for i in range(1, 6):
    print('*' * i)

# Inverted Right-Angled Triangle
for i in range(5, 0, -1):
    print('#' * i)

# Pyramid
for i in range(1, 10, 2):
    print(('$' * i).center(9))

# Inverted Pyramid
for i in range(9, 0, -2):
    print(('@' * i).center(9))

# Diamond
# Upper part
for i in range(1, 10, 2):
    print(('&' * i).center(9))
# Lower part
for i in range(7, 0, -2):
    print(('&' * i).center(9))

# Square
for i in range(5):
    print('%' * 5)

# Rotated Right-Angled Triangle
for i in range(1, 6):
    print('+' * i)




