import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Co dictionary concentration and abs
Codata = {
    'Concentration': [0.0376, 0.0752, 0.1128, 0.1504],
    'Co_410': [0.03732, -0.01443, 0.0129, 0.0266],
    'Co_450': [0.18649, 0.06469, 0.21712, 0.29409],
    'Co_510': [0.41485, 0.18503, 0.52834, 0.70183],
    'Co_540': [0.26119, 0.10986, 0.32408, 0.43262],
    'Co_575': [0.05976, 0.01002, 0.05575, 0.07893],
    'Co_624': [0.03341, -0.00194, 0.02041, 0.03118],
    '15%T': [0.8239, 0.8239, 0.8239, 0.8239], #This has been converted to Abs
    '65%T': [0.187, 0.187, 0.187, 0.187],
}

#Convert to DataFrame
df_co = pd.DataFrame(Codata)

#Cr dictionary, concentration and abs
Crdata = {
    'Concentration': [0.01, 0.02, 0.03, 0.04],
    'Cr_410': [0.14911, 0.36527, 0.46527, 0.6051],
    'Cr_450': [0.07125, 0.17801, 0.21561, 0.27514],
    'Cr_510': [0.04101, 0.11951, 0.14582, 0.18954],
    'Cr_540': [0.08861, 0.22317, 0.28638, 0.3729],
    'Cr_575': [0.1259,0.30304, 0.39408, 0.51295],
    'Cr_624': [0.07208, 0.17820, 0.22847, 0.29523],
    '15%T': [0.8239, 0.8239, 0.8239, 0.8239], #This has been converted to Abs
    '65%T': [0.187, 0.187, 0.187, 0.187],
}

#Convert to DataFrame
#df_cr = pd.DataFrame(Crdata)


# Data
x = df_co['Concentration']
y = df_co['Co_410']
y0 = df_co['Co_450']
y1 = df_co['Co_510']
y2 = df_co['Co_540']
y3 = df_co['Co_575']
y4 = df_co['Co_624']
y_15 = df_co['15%T'].values
y_65 = df_co['65%T'].values

#Calculate the Fit
# The '1' means "Degree 1" (which is a straight line)
# It returns the Slope (m) and Intercept (b)
slope, intercept = np.polyfit(x, y, 1)
slope0, intercept0 = np.polyfit(x, y0, 1)
slope1, intercept1 = np.polyfit(x, y1, 1)
slope2, intercept2 = np.polyfit(x, y2, 1)
slope3, intercept3 = np.polyfit(x, y3, 1)
slope4, intercept4 = np.polyfit(x, y4, 1)


print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"Equation: y = {slope0:.2f}x + {intercept0:.2f}")
print(f"Equation: y = {slope1:.2f}x + {intercept1:.2f}")
print(f"Equation: y = {slope2:.2f}x + {intercept2:.2f}")
print(f"Equation: y = {slope3:.2f}x + {intercept3:.2f}")
print(f"Equation: y = {slope4:.2f}x + {intercept4:.2f}")

# Plot
plt.figure(figsize=(10, 6))

plt.plot(df_co['Concentration'], df_co['15%T'], label='15 %T')
plt.plot(df_co['Concentration'], df_co['65%T'], label='65 %T')


plt.plot(x, y, 'o', label='Co 410nm', color='blue') # Scatter plot
plt.plot(x, y0, 'o', label='Co 450nm', color='orange') # Scatter plot
plt.plot(x, y1, 'o', label='Co 510nm', color='green') # Scatter plot
plt.plot(x, y2, 'o', label='Co 540nm', color='red') # Scatter plot
plt.plot(x, y3, 'o', label='Co 575nm', color='magenta') # Scatter plot
plt.plot(x, y4, 'o', label='Co 624nm', color='brown') # Scatter plot

# Plot the line using the formula y = mx + b
plt.plot(x, slope * x + intercept, label='Co 410nm Fit', color='blue', linestyle=':')
plt.plot(x, slope0 * x + intercept0, label='Co 450nm Fit', color='orange', linestyle=':')
plt.plot(x, slope1 * x + intercept1, label='Co 510nm Fit', color='green', linestyle=':')
plt.plot(x, slope2 * x + intercept2, label='Co 540nm Fit', color='red', linestyle=':')
plt.plot(x, slope3 * x + intercept3, label='Co 575nm Fit', color='magenta', linestyle=':')
plt.plot(x, slope4 * x + intercept4, label='Co 624nm Fit', color='brown', linestyle=':')

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True)
plt.title('Co Calibration Curves')
plt.xlabel('Concentration (M)')
plt.ylabel('Absorbance (Abs)')
plt.tight_layout()
# --- PLOT SAVE COMMAND ---
# dpi=300 makes it high resolution (good for papers/slides)
# bbox_inches='tight' prevents axis labels from getting cut off
plt.savefig('CoLinearCalCurves.png', dpi=300, bbox_inches='tight')

plt.show()
