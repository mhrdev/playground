[![Build Status](https://travis-ci.org/mhrdev/playground.svg?branch=master)](https://travis-ci.org/mhrdev/playground)

# Usage

````
>>> from triangle.triangle import get_triangle_type
>>> get_triangle_type(5, 10, 8)
'SCALENE'
>>> get_triangle_type(5.5, 5.5, 5.5)
'EQUILATERAL'
>>> get_triangle_type(1, 2, 3)
'SCALENE'
>>> get_triangle_type(1, 1, 30)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "triangle/triangle.py", line 38, in get_triangle_type
    _validate_sides(a, b, c)
  File "triangle/triangle.py", line 26, in _validate_sides
    raise ValueError("sum of 2 shortes sides must greater or equals the longest side")
ValueError: sum of 2 shortes sides must greater or equals the longest side
````
