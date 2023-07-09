import numpy as np
import pandas as pd
from statsmodels.stats.weightstats import _tconfint_generic as t_stat
x_mean = 174.2
x_std = np.sqrt(25)
x_mean_std = x_std / np.sqrt(27)
t_stat(x_mean, x_mean_std, 27 - 1, 0.05, 'two-sided')