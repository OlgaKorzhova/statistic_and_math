from math import factorial
def bernulli(n, k, p):
    comb=factorial(n)/(factorial(k)*factorial(n-k))
    return comb*(p**k)*(1-p)**(n-k)
print(f'Вероятность, что орел выпадет 70 раз = {bernulli(144,70,0.5): .5f}')