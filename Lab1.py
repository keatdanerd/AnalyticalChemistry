import pandas as pd
import matplotlib.pyplot as plt


#Start data analyzation
my_cols = range(611)

# Import dataframe
df = pd.read_csv('Data/AChemFiles/Co2+ Cr2+ Unknown.20260115.14.56.49.CSV', header=None, names=my_cols)
print("Shape:", df.shape) #is (3, 611)
print(df.iloc[:, 0]) #reveals that row 0 has text

#This selects row index 1 and row index 2 only (data)
data_rows = df.iloc[1:3, :]

#Transpose the selected columns to become X and Y var
df_plot = data_rows.T
df_plot.columns = ['X_Data', 'Y_Data']

# --- CRITICAL FIX START ---
# Force columns to be numbers. 'coerce' turns any non-numbers into NaN (safe to ignore)
df_plot['X_Data'] = pd.to_numeric(df_plot['X_Data'], errors='coerce')
df_plot['Y_Data'] = pd.to_numeric(df_plot['Y_Data'], errors='coerce')
# --- CRITICAL FIX END ---

#cutoff the messy data at the beginning of the plot
start_value = 260 #or whatever value
df_trimmed = df_plot[df_plot['X_Data'] > start_value]

#Plot the data
plt.figure(figsize = (10,10))
plt.plot(df_trimmed['X_Data'], df_trimmed['Y_Data'])
#plt.plot(df_plot['X_Data'], df_plot['Y_Data'])
plt.title('UV-Vis of Unknown Co/Cr Solution')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance (Abs)')
plt.grid(True)

# --- PLOT SAVE COMMAND ---
# dpi=300 makes it high resolution (good for papers/slides)
# bbox_inches='tight' prevents axis labels from getting cut off
plt.savefig('UnkCoCr.png', dpi=300, bbox_inches='tight')

plt.show()