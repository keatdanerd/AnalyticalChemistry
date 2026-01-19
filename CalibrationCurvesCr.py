import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


#Create a "Dictionary" of data
Crdata = {
    'Concentration': [0.01, 0.02, 0.03, 0.04],
    'Cr_410': [0.14911, 0.36527, 0.46527, 0.6051],
    'Cr_450': [0.07125, 0.17801, 0.21561, 0.27514],
    'Cr_510': [0.04101, 0.11951, 0.14582, 0.18954],
    'Cr_540': [0.08861, 0.22317, 0.28638, 0.3729],
    'Cr_575': [0.1259,0.30304, 0.39408, 0.51295],
    'Cr_624': [0.07208, 0.17820, 0.22847, 0.29523],
}

#Convert to DataFrame
df_manual = pd.DataFrame(Crdata)

#The y data is separated by wavelength, the values are in Abs
x_data = df_manual['Concentration'].values
y_data_410 = df_manual['Cr_410'].values
y_data_450 = df_manual['Cr_450'].values
y_data_510 = df_manual['Cr_510'].values
y_data_540 = df_manual['Cr_540'].values
y_data_575 = df_manual['Cr_575'].values
y_data_624 = df_manual['Cr_624'].values

#Define the Exponential Function
def exponential_model(x, a, b, c):
    return a * np.exp(b * x) + c

# Fit the curve, need to define popt for each y data set
# p0 is the "initial guess" for a, b, c (helps the math solver)
initial_guess = [1, 1, 1]
popt, pcov = curve_fit(exponential_model, x_data, y_data_410, p0=initial_guess, maxfev=5000)
popt0, pcov = curve_fit(exponential_model, x_data, y_data_450, p0=initial_guess, maxfev=5000)
popt1, pcov = curve_fit(exponential_model, x_data, y_data_510, p0=initial_guess, maxfev=5000)
popt2, pcov = curve_fit(exponential_model, x_data, y_data_540, p0=initial_guess, maxfev=5000)
popt3, pcov = curve_fit(exponential_model, x_data, y_data_575, p0=initial_guess, maxfev=5000)
popt4, pcov = curve_fit(exponential_model, x_data, y_data_624, p0=initial_guess, maxfev=5000)

# popt contains your optimized [a, b, c] values
a_opt, b_opt, c_opt = popt
print(f"Equation: y = {a_opt:.3f} * e^({b_opt:.3f}x) + {c_opt:.3f}")
a_opt, b_opt, c_opt = popt0
print(f"Equation: y = {a_opt:.3f} * e^({b_opt:.3f}x) + {c_opt:.3f}")
a_opt, b_opt, c_opt = popt1
print(f"Equation: y = {a_opt:.3f} * e^({b_opt:.3f}x) + {c_opt:.3f}")
a_opt, b_opt, c_opt = popt2
print(f"Equation: y = {a_opt:.3f} * e^({b_opt:.3f}x) + {c_opt:.3f}")
a_opt, b_opt, c_opt = popt3
print(f"Equation: y = {a_opt:.3f} * e^({b_opt:.3f}x) + {c_opt:.3f}")
a_opt, b_opt, c_opt = popt4
print(f"Equation: y = {a_opt:.3f} * e^({b_opt:.3f}x) + {c_opt:.3f}")

# Generate the Smooth Trendline
# Create a smooth range of X values from min to max
x_trend = np.linspace(min(x_data), max(x_data), 100)
y_trend_410 = exponential_model(x_trend, *popt)
y_trend_450 = exponential_model(x_trend, *popt0)
y_trend_510 = exponential_model(x_trend, *popt1)
y_trend_540 = exponential_model(x_trend, *popt2)
y_trend_575 = exponential_model(x_trend, *popt3)
y_trend_624 = exponential_model(x_trend, *popt4)

# Plot
plt.plot(df_manual['Concentration'], df_manual['Cr_410'], label='Cr 410nm')
plt.plot(df_manual['Concentration'], df_manual['Cr_450'], label='Cr 450nm')
plt.plot(df_manual['Concentration'], df_manual['Cr_510'], label='Cr 510nm')
plt.plot(df_manual['Concentration'], df_manual['Cr_540'], label='Cr 540nm')
plt.plot(df_manual['Concentration'], df_manual['Cr_575'], label='Cr 575nm')
plt.plot(df_manual['Concentration'], df_manual['Cr_624'], label='Cr 624nm')
plt.plot(x_trend, y_trend_410, color='blue', linestyle=':', label='Cr 410nm Fit') # Line for fit
plt.plot(x_trend, y_trend_450, color='orange', linestyle=':', label='Cr 450nm Fit')
plt.plot(x_trend, y_trend_510, color='green', linestyle=':', label='Cr 510nm Fit')
plt.plot(x_trend, y_trend_540, color='red', linestyle=':', label='Cr 540nm Fit')
plt.plot(x_trend, y_trend_575, color='magenta', linestyle=':', label='Cr 575nm Fit')
plt.plot(x_trend, y_trend_624, color='brown', linestyle=':', label='Cr 624nm Fit')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True)
plt.title('Cr Calibration Curves')
plt.xlabel('Concentration (M)')
plt.ylabel('Absorbance (Abs)')
plt.tight_layout()

# --- PLOT SAVE COMMAND ---
# dpi=300 makes it high resolution (good for papers/slides)
# bbox_inches='tight' prevents axis labels from getting cut off
plt.savefig('CrCalibrationCurves.png', dpi=300, bbox_inches='tight')


plt.show()
