def func2(num: str) -> float:
    real, frac = num.split('.')
    number = int(real)
    for i in range(1, len(frac)):
        number += int(frac[i])*10**(-i)
    return number


print(func2('3.13123123'))