from math import exp
from math import factorial
def poisson_distr(m,p,n):
    lamb=p*n
    return exp(-lamb)*(lamb**m)/factorial(m)
print(f'Вероятность, что не перегорит ни одна лампа = {poisson_distr(0,0.0004,5000): .5f}')
print(f'Вероятность, что перегорят 2 лампы в один день = {poisson_distr(2,0.0004,5000): .5f}')