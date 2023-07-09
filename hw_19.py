import numpy as np
import scipy.stats as stats
x1 = np.array([150, 160, 165, 145, 155])
x2 = np.array([140, 155, 150, 130, 135])
stats.wilcoxon(x1, x2)
#Cтатистически значимых различий не обнаружено на уровне значимости alpha = 0.05