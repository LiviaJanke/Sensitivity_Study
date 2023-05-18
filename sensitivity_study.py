
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:32:30 2023

@author: lme19
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

#%%

df_original = pd.read_csv('no_PCA_v2.ASC', skiprows = 8, delimiter = '\t')


date_and_time = df_original['# Date (DD/MM/YYYY)'] + ' ' + df_original['Time (hh:mm:ss)']

datetime = pd.to_datetime(df_original['# Date (DD/MM/YYYY)'] + ' ' + df_original['Time (hh:mm:ss)'])

df_original['Date_Time'] = datetime


#corrected_df = test1_df.drop([2368])

#%%

#Getting rid of the spectrum that was used as the reference since it creates an anomaly

#df_no_reference = df_original[df_original.Date_Time != '2022-08-23 22:00:05']

df_no_reference = df_original[df_original.Date_Time != '2022-08-23 22:00:05']

df_no_reference.plot(x = 'Date_Time', y = 'Test.SlCol(O3)', yerr = 'Test.SlErr(O3)', linewidth = 0, marker = '.') 

df_no_reference.plot(x = 'Date_Time', y = 'Test.SlCol(NO2)',  yerr = 'Test.SlErr(NO2)')


#%%

#Filtering out points which take less than 30 scans into consideration

df_high_scans = df_no_reference[df_no_reference.Scans > 30]

df_high_scans.plot(x = 'Date_Time', y = 'Test.SlCol(O3)', yerr = 'Test.SlErr(O3)', linewidth = 0, marker = '.') 

df_high_scans.plot(x = 'Date_Time', y = 'Test.SlCol(NO2)',  yerr = 'Test.SlErr(NO2)')

#Does seem to remove a lot of the noise!!

#%%


#focusing on the stable section after 22:00

lower_lim = 1500
upper_lim = 3360

#separate sections for waves and SCD


stable_Datetime = df_high_scans['Date_Time'][lower_lim:upper_lim]
stable_SZA = df_high_scans['SZA'][lower_lim:upper_lim]
stable_SlCol_O3 = df_high_scans['Test.SlCol(O3)'][lower_lim:upper_lim]
stable_SlErr_O3 = df_high_scans['Test.SlErr(O3)'][lower_lim:upper_lim]
stable_SlCol_NO2 = df_high_scans['Test.SlCol(NO2)'][lower_lim:upper_lim]
stable_SlErr_NO2 = df_high_scans['Test.SlErr(NO2)'][lower_lim:upper_lim]
stable_RMS = df_high_scans['Test.RMS'][lower_lim:upper_lim]
stable_CLD = df_high_scans['Test.SlCol(CLD)'][lower_lim:upper_lim]
stable_CLD_error = df_high_scans['Test.SlErr(CLD)'][lower_lim:upper_lim]


stable_SlCol_IO = df_high_scans['Test.SlCol(IO)'][lower_lim:upper_lim]
stable_SlErr_IO = df_high_scans['Test.SlErr(IO)'][lower_lim:upper_lim]

#%%

plt.errorbar(stable_Datetime, stable_SlCol_O3, yerr = stable_SlErr_O3, linewidth = 0, ecolor = 'red', elinewidth = 0.1, marker = '.', color = 'black', capsize = 1, markersize = 0.5)
plt.title('SlCol(O3)')
plt.xlabel('Date Time')
plt.ylabel('SlCol(O3)')
plt.show()


#%%

plt.errorbar(stable_Datetime, stable_SlCol_NO2, yerr = stable_SlErr_NO2, linewidth = 0, ecolor = 'red', elinewidth = 0.1, marker = '.', capsize = 1, markersize = 0.5, color = 'black')
plt.title('SlCol(NO2)')
plt.xlabel('Date Time')
plt.ylabel('SlCol(NO2)')
plt.show()

#%%

plt.errorbar(stable_Datetime, stable_SlCol_IO, yerr = stable_SlErr_IO, linewidth = 0, ecolor = 'red', elinewidth = 0.1, marker = '.', capsize = 1, markersize = 0.5, color = 'black')
plt.title('SlCol(IO)')
plt.xlabel('Date Time')
plt.ylabel('SlCol(NO2)')
plt.show()



#%%

plt.rcParams.update({'font.size': 5})
  
# Initialise the subplot function using number of rows and columns
figure, axis = plt.subplots(5, 1)
  

axis[0].errorbar(stable_SZA, stable_SlCol_O3,  yerr = (stable_SlErr_O3 * 2), linewidth = 0, ecolor = 'red', elinewidth = 0.1, marker = '.', color = 'black', capsize = 1, markersize = 0.5)
axis[0].set_title('SlCol(O3)')
#axis[0].yscale
axis[0].grid()
  

axis[1].errorbar(stable_SZA, stable_SlCol_NO2, yerr = (stable_SlErr_NO2 * 2), linewidth = 0, ecolor = 'red', elinewidth = 0.1, marker = '.', capsize = 1, markersize = 0.5, color = 'black')
axis[1].set_title('SlCol(NO2)')
axis[1].grid()

axis[2].errorbar(stable_SZA, stable_SlCol_IO, yerr = (stable_SlErr_IO * 2), linewidth = 0, ecolor = 'red', elinewidth = 0.1, marker = '.', capsize = 1, markersize = 0.5, color = 'black')
axis[2].set_title('SlCol(IO)')
axis[2].grid()
  

axis[3].plot(stable_SZA, stable_RMS)
axis[3].set_title('RMS')
axis[3].grid()
  

axis[4].errorbar(stable_SZA, stable_CLD, yerr = stable_CLD_error, linewidth = 0, ecolor = 'red', elinewidth = 0.1, marker = '.', capsize = 1, markersize = 0.5, color = 'black')
axis[4].set_title("CLD")
axis[4].grid()

plt.subplots_adjust(hspace=0.7)
plt.xlabel('SZA (degrees)')

  
# Combine all the operations and display
plt.savefig('no_PCA_v2.png', dpi=300)

plt.show()


#%%


#plt.subplot(311)
#plt.errorbar(stable_SZA, stable_SlCol_O3,  yerr = (stable_SlErr_O3 * 2), linewidth = 0, ecolor = 'red', elinewidth = 0.1, marker = '.', color = 'black', capsize = 1, markersize = 0.5)
#plt.xscale('symlog')
#plt.ylabel('symlogx')
#plt.grid(True)
#plt.title('SlCol(O3)')
#plt.gca().xaxis.grid(True, which='minor')  # minor grid on too


#plt.subplot(312)
#plt.errorbar(stable_SZA, stable_SlCol_NO2, yerr = (stable_SlErr_NO2 * 2), linewidth = 0, ecolor = 'red', elinewidth = 0.1, marker = '.', capsize = 1, markersize = 0.5, color = 'black')
#plt.yscale('symlog')
#plt.ylabel('symlogy')
#plt.title('SlCol(NO2)')

#plt.subplot(313)
#plt.errorbar(stable_SZA, stable_SlCol_IO, yerr = (stable_SlErr_IO * 2), linewidth = 0, ecolor = 'red', elinewidth = 0.1, marker = '.', capsize = 1, markersize = 0.5, color = 'black')
#plt.xscale('symlog')
#plt.yscale('symlog')
#plt.grid(True)
#plt.ylabel('symlog both')


#%%

#plt.subplot(312)
#plt.plot(y, x)
#plt.yscale('symlog')
#plt.ylabel('symlogy')

#plt.subplot(313)
#plt.plot(x, np.sin(x / 3.0))
#plt.xscale('symlog')
#plt.yscale('symlog', linthreshy=0.015)
#plt.grid(True)
#plt.ylabel('symlog both')

#plt.tight_layout()
#plt.show()



#%%

print(df_high_scans.describe())

vital_stats = df_high_scans.describe()

vital_stats.to_csv('no_PCA_v2.txt', header = True, index = True, sep=',')


print(vital_stats['Test.RMS'])


#%%









































