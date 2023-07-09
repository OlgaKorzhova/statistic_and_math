import numpy as np
import pandas as pd
from statsmodels.stats.weightstats import _tconfint_generic as t_stat
x = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
x_mean = x.mean()
x_std = x.std(ddof = 1)
x_mean_std = x_std / (np.sqrt(len(X)))
t_stat(x_mean, x_mean_std, len(X) - 1, 0.05, 'two-sided')