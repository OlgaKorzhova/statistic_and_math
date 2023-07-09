import numpy as np
import scipy.stats as stats
x1 = np.array([150, 160, 165, 145, 155])
x2 = np.array([140, 155, 150, 130, 135])
x3 = np.array([130, 130, 120, 130, 125])
stats.friedmanchisquare(x1, x2, x3)
#pvalue < alpha, H0 - отвергается с ошибкой alpha = 0.05, принимается гипотиза Н1 - различия есть