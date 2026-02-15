import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Dictionary concentration and rate constants
SetBdata = {
    'Concentration': [0, 0.11, 0.22, 0.44, 0.55,],
    'Rates': [0.0034, 0.0042, 0.0032, 0.0063, 0.0075],


}

#Convert to DataFrame
df_set = pd.DataFrame(SetBdata)

# Data
x = df_set['Concentration']
y = df_set['Rates']


#Calculate the Fit
# The '1' means "Degree 1" (which is a straight line)
# It returns the Slope (m) and Intercept (b)
slope, intercept = np.polyfit(x, y, 1)
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")

y_predicted = slope * x + intercept

# 3. Calculate R^2 manually
residuals = y - y_predicted
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y - np.mean(y))**2)

r_squared = 1 - (ss_res / ss_tot)

# Plot
plt.figure(figsize=(10, 6))

plt.plot(x, y, 'o', label='Data Points', color='blue') # Scatter plot

# Plot the line using the formula y = mx + b
plt.plot(x, slope * x + intercept, label=f"y = {slope:.2f}x + {intercept:.2f}, R² = {r_squared:.4f}", color='green', linestyle='--')

plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.20), borderaxespad=0.)
plt.grid(True)
plt.title('Set C Rate vs. [HCl]')
plt.xlabel('Concentration (M)')
plt.ylabel('Rate Constant')
plt.tight_layout()
# --- PLOT SAVE COMMAND ---
# dpi=300 makes it high resolution (good for papers/slides)
# bbox_inches='tight' prevents axis labels from getting cut off
plt.savefig('Set C Rate vs. Concentration.png', dpi=300, bbox_inches='tight')

plt.show()
