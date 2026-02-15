import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Import dataframe without headers
file_path = 'Data/AChemFiles3/Set B Asc 0.0167M.20260205.14.50.10.CSV'
df = pd.read_csv(file_path, header=None, skiprows=1)

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
min_wave = 100
max_wave = 750

# 2. Create a "mask" (True for values we want, False for noise)
mask = (wavelengths >= min_wave) & (wavelengths <= max_wave)

# 3. Apply the mask to both X and Y
wavelengths_trimmed = wavelengths[mask]
absorbance_trimmed = absorbance_data[:, mask] # Slices all rows, but only masked columns

# 4. Now Plot the trimmed version
plt.figure(figsize=(10, 6))
for i in range(len(absorbance_trimmed)):
    plt.plot(wavelengths_trimmed, absorbance_trimmed[i], label=f'Scan {i+1}')
plt.title('Set A 3.9E-5 M MB+')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance (Abs)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.xlim(min_wave, max_wave) # Forces the graph window to match

# --- PLOT SAVE COMMAND ---
# dpi=300 makes it high resolution (good for papers/slides)
# bbox_inches='tight' prevents axis labels from getting cut off
#plt.savefig('Co0.0752M.png', dpi=300, bbox_inches='tight')

plt.show()


