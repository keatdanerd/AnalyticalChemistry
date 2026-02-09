import numpy as np
import pandas as pd

# %T = 10^-Abs *100

#Crdata = {
#    'Concentration': [0.01, 0.02, 0.03, 0.04],
#    'Cr_410': [0.14911, 0.36527, 0.46527, 0.6051],
#    'Cr_450': [0.07125, 0.17801, 0.21561, 0.27514],
#    'Cr_510': [0.04101, 0.11951, 0.14582, 0.18954],
#    'Cr_540': [0.08861, 0.22317, 0.28638, 0.3729],
#    'Cr_575': [0.1259,0.30304, 0.39408, 0.51295],
#    'Cr_624': [0.07208, 0.17820, 0.22847, 0.29523],
#}

#df_absorbance = pd.DataFrame(Crdata)

#perT = 10**(-df_absorbance['15%T'].values)*100

#print(perT)

# Abs = -log(%T*0.01)

import math

print(abs(math.log10(0.15)))
print(abs(math.log10(0.65)))

