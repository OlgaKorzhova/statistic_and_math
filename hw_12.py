import numpy as np
from scipy import stats
x_1 = np.array([172, 177, 158, 170, 178, 175, 164, 160, 169])
x_2 = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])

stats.ttest_rel(x_1, x_2)