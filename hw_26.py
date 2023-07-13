import numpy as np
import matplotlib.pyplot as plt
alpha = 1e-6
b1 = 0.1
def mse_(b1, y=ks, X=zp, n=10):
    return np.sum((b1 * X - y) ** 2) / n
for i in range(1000):
    fp = (1 / n) * np.sum(2 * (b1 * zp - ks) * zp)
    b1 -= alpha * fp
    if i % 100 == 0:
        print(f'Итерация: {i}, b1 : {b1}, mse: {mse_(b1) }')
y_pred2 = b1 * zp
y_pred2
plt.scatter(zp, ks)
plt.plot(zp, y_pred, 'b:', label = 'с intercept')
plt.plot(zp, y_pred2, 'r:', label = 'без intercept')
plt.legend()