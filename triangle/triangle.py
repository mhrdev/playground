EQUILATERAL = 1
ISOSCELES = 2
SCALENE = 3

def _is_number(x):
    return isinstance(x, ( int, long, float ) )

def _validate_sides(a,b,c):
    """Validate sides can make a valid triangle"""

    if not a or not b or not c:
        raise ValueError("Sides cannot have None value")

    if not (_is_number(a) and _is_number(b) and _is_number(c)):
        raise ValueError("All side must be numbers")

    if a<=0 or b<=0 or c<=0:
        raise ValueError("All sides lengths must have positive values")

    if a+b < c or \
        a+c < b or \
        b+c < a:
        raise ValueError("sum of 2 shortes sides must greater or equals the longest side")

def get_triangle_type(a, b, c):
    """Get triangle type
    :params: a: side a
    :params: b: side b
    :params: c: side c

    :return: type of triangle
    """

    _validate_sides(a,b,c)

    if a == b == c:
        return EQUILATERAL

    if a == b or a == c or b == c:
        return ISOSCELES

    return SCALENE
