import numpy as np
from statsmodels.stats.weightstats import _tconfint_generic as t_stat
from scipy import stats
m = 80
sigma = 16
n = 256
p = 0.95
alpha = 0.05
z = stats.norm.ppf(alpha/2)
(m - z * sigma / np.sqrt(n), m + z * sigma / np.sqrt(n))