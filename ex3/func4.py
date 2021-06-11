def gcd(x, y):
    if(x < y):
        temp = x
        x = y
        y = temp
    while (y != 0):
        r = x % y
        x = y
        y = r
    r = x
    return r


def sim(a: tuple):
    g = gcd(a[0], a[1])
    return (a[0]/g, a[1]/g)


def sim_list(l: list):
    results = []
    for item in l:
        results.append(sim(item))
    return results


print(sim_list([(1, 2), (2, 4), (4, 16), (8, 12)]))
