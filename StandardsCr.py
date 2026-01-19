from fileinput import filename

import pandas as pd
import matplotlib.pyplot as plt

#import all the csv files and name them
# Format: 'Actual_Filename.csv' : 'My name'
files_to_plot = {
    'Data/AChemFiles/Cr(NO3)3 0.01M.20260115.14.32.34.CSV': 'Cr 0.01M',
    'Data/AChemFiles/Cr(NO3)3.0.02 M.20260115.14.14.58.CSV': 'Cr 0.02M',
    'Data/AChemFiles/Cr(NO3)3 0.03M.20260115.14.35.38.CSV': 'Cr 0.03M',
    'Data/AChemFiles/Cr(NO3)3 0.04M.20260115.14.37.08.CSV': 'Cr 0.04M',
}

plt.figure(figsize=(10,10))

#Clean all the files in a loop
# .items() gives the filename and the label
for filename, custom_label in files_to_plot.items():

    #load the file and force the columns
    df = pd.read_csv(filename, header=None, names=range(611))

    #Transform
    data_rows = df.iloc[1:3, :]
    df_t = data_rows.T
    df_t.columns = ['x', 'y']

    #convert to numbers (CRITICAL STEP!)
    df_t['x'] = pd.to_numeric(df_t['x'], errors='coerce')
    df_t['y'] = pd.to_numeric(df_t['y'], errors='coerce')



    # cutoff the messy data at the beginning of the plot
    start_value = 260  # or whatever value
    df_trimmed = df_t[df_t['x'] > start_value]

    plt.plot(df_trimmed['x'], df_trimmed['y'], label=custom_label)

#Final Plot
plt.legend()
plt.title('Absorbance vs Wavelength for the Cr Standards')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance (Abs)')
plt.grid(True)

# --- PLOT SAVE COMMAND ---
# dpi=300 makes it high resolution (good for papers/slides)
# bbox_inches='tight' prevents axis labels from getting cut off
#plt.savefig('OverlayedStandardCrSolns.png', dpi=300, bbox_inches='tight')

#plt.show()
