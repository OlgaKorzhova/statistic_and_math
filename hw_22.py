import numpy as np
import pandas as pd
from statsmodels.stats.weightstats import _tconfint_generic as t_stat
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array( [401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
M_X = zp.mean()
M_Y = ks.mean()
M_XY = (zp * ks).mean()
cov_ks = M_XY - M_X * M_Y
cov_ks
np.cov(zp, ks, ddof = 0)
cov_ks2 = ((zp - zp.mean()) * (ks - ks.mean())).mean()
cov_ks2
std_X = zp.std()
std_Y = ks.std()
corr_ks = cov_ks / (std_X * std_Y)
corr_ks
np.corrcoef(zp, ks)