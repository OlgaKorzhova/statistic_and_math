import numpy as np
from scipy import stats
fp = np.array([173, 175, 180, 178, 177, 185, 183, 182], dtype = np.float64)
hp = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180], dtype = np.float64)
wl = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170], dtype = np.float64)
n1 = fp.shape[0]
n2 = hp.shape[0]
n3 = wl.shape[0]
fp_mean = fp.mean()
hp_mean = hp.mean()
wl_mean = wl.mean()
print(f"Среднее значение роста футболистов = {fp_mean:.3f}")
print(f"Среднее значение роста хоккеистов = {hp_mean:.3f}")
print(f"Среднее значение роста штангистов = {wl_mean:.3f}")
y = np.concatenate([fp, hp, wl])
y_mean = y.mean()
print(f"Среднее значение роста всех спортсменов = {y_mean:.3f}")
S2_F = n1 * (fp_mean - y_mean) ** 2 + n2 * (hp_mean - y_mean) ** 2 + n3 * (wl_mean - y_mean) ** 2
S2_res = ((fp - fp_mean) ** 2).sum() + ((hp - hp_mean) ** 2).sum() + ((wl - wl_mean) ** 2).sum()

S2 = ((y - y_mean) ** 2).sum()
print(f" Sf^2 = {S2_F:.3f}")
print(f" Sres^2 = {S2_res:.3f}")
print()
print(f" S^2 = Sf^2 + Sres^2")
print(f"{S2:.3f} = {S2_F + S2_res:.3f}")
k = 3
n = n1 + n2 + n3
k1 = k - 1
k2 = n - k
sigma2_F = S2_F / k1
sigma2_res = S2_res / k2
print(f"Факторная дисперсия = {sigma2_F:.3f}")
print(f"Остаточная дисперсия = {sigma2_res:.3f}")
T = sigma2_F / sigma2_res
print(f"Значение статистики = {T:.3f}")
f = stats.f_oneway(fp, hp, wl)
f
alpha = 0.05

F_crit = stats.f.ppf(1 - alpha, k1, k2)
print(f"Критическое значение = {F_crit:.3f}")
