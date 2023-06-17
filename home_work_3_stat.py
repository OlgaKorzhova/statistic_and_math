from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))
P=combinations(9,3)/combinations(15,3)
print(f'Вероятность, что все три детали окрашены = {round(P,5)}')
