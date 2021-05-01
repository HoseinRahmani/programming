def prog4(n: int):
    gc = []
    for i in range(1, (n/2)+1):
        if n % i == 0:
            gc.append(i)
    return gc
