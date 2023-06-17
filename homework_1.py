from math import factorial
def bernulli(n, k, p):
    comb=factorial(n)/(factorial(k)*factorial(n-k))
    return comb*(p**k)*(1-p)**(n-k)
print(f'Вероятность попадания = {bernulli(100,85,0.8): .5f}')