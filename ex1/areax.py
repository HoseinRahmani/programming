from .area import area


def areax(q: float, a: float = 0, b: float = 0, c: float = 0, d: float = 0):
    values = [a, b, c, d]
    if values.count(0) == 2:
        print('Number of zeros is wrong!')
        return
    values.sort()
    return area(a=values[0], b=values[1], c=values[2], d=values[3], q=q)
