import numpy as np
import matplotlib.pyplot as plt
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = len(ks)
b1 = (np.mean(zp*ks)-np.mean(zp)*np.mean(ks))/(np.mean(zp**2) - np.mean(zp)**2)
b1
b0 = np.mean(ks)-b1*np.mean(zp)
b0
y_pred = b0 + b1 * zp
y_pred
plt.scatter(zp, ks)
plt.plot(zp, y_pred)
mse_ = np.sum(((b0 + b1 * zp) - ks) ** 2 / n)
mse_
mse_ = ((ks - y_pred)**2).sum() / n
mse_


zp1 = zp.reshape(1, n)
ks1 = ks.reshape(1, n)
b1 = np.dot(np.dot(np.linalg.inv(np.dot(zp1, zp1.T)), zp1), ks1.T)[0][0]
b1
y_pred1 = b1 * zp
y_pred1
plt.scatter(zp, ks)
plt.plot(zp, y_pred, 'b', label = 'с intercept')
plt.plot(zp, y_pred1, 'r', label = 'без interсept')
plt.legend()
