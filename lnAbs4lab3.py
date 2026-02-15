import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress # For the linear fit

# 1. Import dataframe without headers
#import all the csv files and name them
# Format: 'Actual_Filename.csv' : 'My name'
files_to_plot = {
    'Data/AChemFiles3/Set C 0 HCl.20260205.15.26.21.CSV' : '0.0M HCl',
    'Data/AChemFiles3/Set C 0.11M HCl.20260205.15.29.21.CSV' : '0.11M HCl',
    'Data/AChemFiles3/Set C 0.22M HCl.20260205.15.32.41.CSV' : '0.22M HCl',
    'Data/AChemFiles3/Set C 0.44M HCl.20260205.15.36.09.CSV' : '0.44M HCl',
    'Data/AChemFiles3/Set C 0.55M HCl.20260205.15.39.47.CSV' : '0.55M HCl',

}

plt.figure(figsize=(12, 10))


for filename, custom_label in files_to_plot.items():

    df = pd.read_csv(filename, header=None, skiprows=1)
    print("Original Shape:", df.shape)

    # 2. Extract Wavelengths (Row 0)
    # We use pd.to_numeric with 'coerce' to turn any "Wavelength" text into NaN, then drop it
    wavelengths = pd.to_numeric(df.iloc[0, :], errors='coerce').dropna().values

    # 3. Extract Absorbance Data (Rows 1 through 13)
    # We slice from row 1 onwards.
    # If your first COLUMN also has text (like "Scan 1"), we slice from column 1 onwards: .iloc[1:, 1:]
    absorbance_data = df.iloc[1:, :].apply(pd.to_numeric, errors='coerce')

    # If the first column was just labels, it will now be NaNs. Let's drop them.
    absorbance_data = absorbance_data.dropna(axis=1, how='all').values

    # 1. Define your desired range (e.g., 400nm to 800nm)
    min_wave = 500
    max_wave = 750

    # 2. Create a "mask" (True for values we want, False for noise)
    mask = (wavelengths >= min_wave) & (wavelengths <= max_wave)

    # 3. Apply the mask to both X and Y
    wavelengths_trimmed = wavelengths[mask]
    absorbance_trimmed = absorbance_data[:, mask] # Slices all rows, but only masked columns

    # --- 1. SETUP TIME ---
    # Replace this list with your actual time values (e.g., [0, 60, 120...])
    time_intervals = np.arange(0, 120, 10)

    # --- 2. FIND PEAK & EXTRACT DATA ---
    # Let's use the first scan (row 0 of absorbance_data) to find the peak index
    peak_idx = np.argmax(absorbance_trimmed[0, :])
    peak_wavelength = wavelengths[mask][peak_idx]

    # Extract the absorbance at this peak for ALL 13 scans
    peak_abs_values = absorbance_trimmed[:, peak_idx]

    # --- 3. CALCULATE LN(ABS) ---
    ln_abs = np.log(peak_abs_values)

    print(f'Peak wavelength: {peak_wavelength:.1f} nm')


    # --- 4. LINEAR REGRESSION (Finding 'k') ---
    slope, intercept, r_value, p_value, std_err = linregress(time_intervals, ln_abs)
    print(f"Rate Constant (k) = {-slope:.4f}")  # Slope is -k

    # --- 5. PLOTTING ---

    plt.scatter(time_intervals, ln_abs, label=custom_label)
    plt.plot(time_intervals, slope * time_intervals + intercept, color='black',
             label=f'Linear Fit (R²={r_value**2:.4f})', linestyle='--')

plt.title(f'Set C Kinetics at {peak_wavelength:.1f} nm')
plt.xlabel('Time (seconds)')
plt.ylabel('ln(Abs)')
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.12),
           ncol=5, # Arranges the labels in 3 columns so it stays horizontal
           frameon=True)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# --- PLOT SAVE COMMAND ---
# dpi=300 makes it high resolution (good for papers/slides)
# bbox_inches='tight' prevents axis labels from getting cut off
#plt.savefig('Set C Kinetics', dpi=300, bbox_inches='tight')

plt.show()