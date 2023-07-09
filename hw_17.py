import numpy as np
import scipy.stats as stats
x1 = np.array([380, 420, 290])
y1 = np.array([140, 360, 200, 900])
stats.mannwhitneyu(x1, y1)
# pvalue > alpha, H0 - не отвергается с ошибкой alpha = 0.05, выборки статистически одинаковые