def prog2():
    x = input('Enter first number')
    y = input('Enter second number')
    results = []
    if x >= y:
        for i in range(y, x+1):
            if i % 2 == 0:
                results.append(i)
    elif x < y:
        for i in range(x, y+1):
            if i % 2 == 0:
                results.append(i)
    return results
