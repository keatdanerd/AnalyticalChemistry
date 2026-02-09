import pandas as pd


#Start data analyzation
my_cols = range(611)

# Import dataframe
df = pd.read_csv('Data/AChemFiles2/Sodium phenolate in MeOH.20260122.14.41.59.CSV', header=None, names=my_cols)
print("Shape:", df.shape) #is (3, 611)
print(df.iloc[:, 0]) #reveals that row 0 has text

#This selects row index 1 and row index 2 only (data)
data_rows = df.iloc[1:3, :]

#Transpose the selected columns to become X and Y var
df_calcs = data_rows.T
df_calcs.columns = ['x', 'y']

# --- CRITICAL FIX START ---
# Force columns to be numbers. 'coerce' turns any non-numbers into NaN (safe to ignore)
df_calcs['x'] = pd.to_numeric(df_calcs['x'], errors='coerce')
df_calcs['y'] = pd.to_numeric(df_calcs['y'], errors='coerce')
# --- CRITICAL FIX END ---

#cutoff the messy data at the beginning of the plot
start_value = 240 #or whatever value
df_trimmed = df_calcs[df_calcs['x'] > start_value]

#define the max values for abs and wavelength
#Find the index (the "row label") where y is at its maximum
max_index = df_trimmed['y'].idxmax()

#Extract the x and y values from df_trimmed at that specific index
max_x = df_trimmed.loc[max_index, 'x']
max_y = df_trimmed.loc[max_index, 'y']

print(f"The max absorbance value is: {max_y}")
print(f"The corresponding wavelength value is: {max_x}")

