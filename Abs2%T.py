import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

pert = np.array([.25, .307, .398, .501, .629, .752, .86, .902, .92, .873, .759, .551, .43, .352])


Abs = -np.log(np.abs(pert))
print(Abs)

Wavelength = np.array([350, 375, 400, 425, 450, 475, 500, 512, 525, 550, 575, 600, 612, 625])

#Plot the data
plt.figure(figsize = (10,10))
plt.plot(Wavelength, Abs)
plt.title('Photometric Response of the Spec20')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance (Abs)')
plt.grid(True, linestyle = ':')

# --- PLOT SAVE COMMAND ---
# dpi=300 makes it high resolution (good for papers/slides)
# bbox_inches='tight' prevents axis labels from getting cut off
#plt.savefig('Spec20photometric.png', dpi=300, bbox_inches='tight')

plt.show()



#%T = 10^-Abs *100

#Spec20data = {
#    'Wavelength': [350, 375, 400, 425, 450, 475, 500, 512, 525, 550, 575, 600, 612, 625],
#    'perT': [25, 30.7, 39.8, 50.1, 62.9, 75.2, 86, 90.2, 92, 87.3, 75.9, 55.1, 43, 35.2],
#}

#df_absorbance = pd.DataFrame(Spec20data)

#perT = 10**(-df_absorbance['15%T'].values)*100

#print(perT)

#Abs = -log(%T*0.01)
#Abs = -(math.log10('perT'*0.01))

#print(Abs)

#print((math.log10(df_absorbance['perT']*0.01)))
#print(abs(math.log10(0.65)))

