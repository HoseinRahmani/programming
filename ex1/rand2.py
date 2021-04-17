import random


def rand2(a: int, b: int):
    random_num = 1
    while random_num % 2 != 0:
        random_num = random.randint(a, b+1)
    return random_num
