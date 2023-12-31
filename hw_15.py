a = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
b = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
x_1 = np.mean(a)
x_2 = np.mean(b)
delta = x_1 - x_2
n = len(a)
D1 = np.var(a, ddof = 1)
D2 = np.var(b, ddof = 1)
D = (D1 + D2) / 2
SE = np.sqrt(D/n + D/n)
t = stats.t.ppf(0.975, 2 * (n - 1))
result = (delta - t*SE, delta + t*SE)
print(f"Доверительный интервал: {result}")