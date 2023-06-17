from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))
P=1/combinations(100,2)
print(f'Вероятность, что оба билета выйгрышны = {round(P,5)}')