import pandas as pd
import numpy as np
from math import factorial
data = pd.Series([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
Mean_Salary = data.sum() / data.count()
Mean_Salary
STD_Salary = np.sqrt(((data - Mean_Salary) ** 2).sum() / data.count())
STD_Salary
var_Salary = ((data - Mean_Salary) ** 2).sum() / data.count()
var_Salary
var_Salary_2 = ((data - Mean_Salary) ** 2).sum() / (data.count() - 1)
var_Salary_2