import numpy as np
import matplotlib.pyplot as plt
alpha = 5e-5

b0 = 0.1
b1 = 0.1

def mse_(b0, b1, y = ks, X = zp, n = 10):
    return np.sum((b0 + b1 * X - y) ** 2) / n
for i in range(1000000):
    y_pred3 = b0 + b1 * zp
    b0 -=alpha * (2 / n) * np.sum((y_pred3 - ks))
    b1 -=alpha * (2 / n) * np.sum((y_pred3 - ks)*zp)
    if i % 100000 == 0:
        print(f"Итерация: {i}, b1 : {b1}, b0 : {b0}, mse: {mse_(b0,b1)}")