from math import sqrt


def equation2d(a: float, b: float, c: float):
    """
    an equation is like this: ax^2+bx+c=0
    """
    delta = b**2-4*a*c
    if delta < 0:
        print("equation has no answers.")
        return
    x1 = (-b+sqrt(delta))/2*a
    x2 = (-b-sqrt(delta))/2*a
    if delta == 0:
        print("equation has only one answer")
        return x1
    else:
        print("equation has two answers")
        return x1, x2
