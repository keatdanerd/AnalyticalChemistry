from fileinput import filename

import pandas as pd
import matplotlib.pyplot as plt

#import all the csv files and name them
# Format: 'Actual_Filename.csv' : 'My name'
files_to_plot = {
    'Data/AChemFiles2/Phenol in MeOH.20260122.14.25.45.CSV' : 'Phenol',
    'Data/AChemFiles2/Sodium phenolate in MeOH.20260122.14.41.59.CSV' : 'Sodium Phenoxide',

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
    start_value = 240 # or whatever value
    end_value = 400
    df_trim = df_t[df_t['x'] > start_value]
    df_trimmed = df_trim[df_trim['x'] < end_value]


    plt.plot(df_trimmed['x'], df_trimmed['y'], label=custom_label)

#Final Plot
plt.legend()
plt.title('Absorbance Spectra of Sodium Phenoxide and Phenol')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance (Abs)')
plt.grid(True)

# --- PLOT SAVE COMMAND ---
# dpi=300 makes it high resolution (good for papers/slides)
# bbox_inches='tight' prevents axis labels from getting cut off
#plt.savefig('phenol.png', dpi=300, bbox_inches='tight')

plt.show()
