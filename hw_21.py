import numpy as np
import scipy.stats as stats
X = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
mean = X.mean()
std = X.std(ddof=1)
t_fact = (mean - 2.5) / std * np.sqrt(len(X))
t_fact
n = 10
m = 2.5
t = stats.t.ppf(0.975, 9)
print(f"t теоретическое = {t:.3f}")
t = (mean - m) * np.sqrt(n) / std
print(f"t рассчитываемое = {t:.3f}")
# t теоретическое > t рассчитываемое, нулевая гипотеза верна