def func1(sentence: str) -> list:
    words = list(map(lambda w: w.strip('.'), sentence.split(' ')))
    return words


print(func1('this is a sentence.'))
