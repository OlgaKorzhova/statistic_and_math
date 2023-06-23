def mean_and_dispers(a,b):
    return f'Среднее значение: М(А) = {(a+b)/2: .3f}\nДисперсия: D(A) = {((b-a)**2)/12: .3f}'
print(mean_and_dispers(200,800))