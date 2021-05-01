def prog1():
    x = input('Enter first number')
    y = input('Enter second number')
    results = []
    for i in range(x, y+1):
        if i % 2 == 0:
            results.append(i)
    return results
