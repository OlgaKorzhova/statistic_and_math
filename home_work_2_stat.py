from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))
P=1/combinations(10,3)
print(f'Вероятность открыть дверь с первой попытки = {round(P,5)}')