import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

phone = np.array([157, 155, 127, 95, 71])
I0 = 197

Abs = -np.log(np.abs(phone/I0))
print(Abs)

conc = np.array([0.1, 0.2, 0.25, 0.50, 1.0])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(conc, Abs)

print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"R-squared: {r_value**2:.4f}")

unkabs = -np.log(np.abs(120/I0))
print(unkabs)
unk = (unkabs - 0.16)/0.91

#Plot the data
plt.figure(figsize = (10,10))
plt.plot(conc, slope * conc + intercept, label=f"y = {slope:.2f}x + {intercept:.2f}, R²: {r_value**2:.4f}", color='blue', linestyle=':')
plt.plot(conc, Abs)
plt.scatter(unk, unkabs, s=100 , label = 'Unknown', color='red')
plt.legend(bbox_to_anchor=(0.5, -0.11), loc='lower center', borderaxespad=0.)
plt.title('Calibration Curve of Phone App')
plt.xlabel('Concentration (M)')
plt.ylabel('Absorbance (Abs)')
plt.tight_layout()
plt.grid(True, linestyle = ':')

# --- PLOT SAVE COMMAND ---
# dpi=300 makes it high resolution (good for papers/slides)
# bbox_inches='tight' prevents axis labels from getting cut off
plt.savefig('PhoneVisCalCurve.png', dpi=300, bbox_inches='tight')

plt.show()