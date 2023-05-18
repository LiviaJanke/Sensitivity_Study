# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:32:30 2023

@author: lme19
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%

test1_df = pd.read_csv('test_pseudoabsorbers_interpolated.ASC', skiprows = 8, delimiter = '\t')


#%%

test1_df.plot()

date_and_time = test1_df['# Date (DD/MM/YYYY)'] + ' ' + test1_df['Time (hh:mm:ss)']

datetime = pd.to_datetime(test1_df['# Date (DD/MM/YYYY)'] + ' ' + test1_df['Time (hh:mm:ss)'])


#%%

plt.plot(datetime, test1_df['Test.SlCol(O3)'])
plt.show()

test1_df['Date_Time'] = datetime

#%%

test1_df.plot('Date_Time', 'Test.SlCol(NO2)')
test1_df.plot('Date_Time', 'Test.SlCol(O3)')
test1_df.plot('Date_Time', 'SZA')

#%%

test1_df.plot(x = 'Date_Time')


#%% 

print(test1_df.describe())

vital_stats = test1_df.describe()

#%%

conc_df = test1_df.drop(columns =['# Date (DD/MM/YYYY)', 'Time (hh:mm:ss)', 'Scans', 'Longitude', 'Latitude'])

corrected_df = test1_df.drop([2359])
conc_df2 = conc_df.drop([2359])


#%%
corrected_df.plot(x = 'Date_Time')

#%%
conc_df2.plot(x = 'Date_Time')

#%%

conc_df2.plot(x = 'Date_Time', y = 'Test.SlCol(O3)', yerr = 'Test.SlErr(O3)', linewidth = 0, marker = 'x') 

conc_df2.plot(x = 'Date_Time', y = 'Test.SlCol(NO2)',  yerr = 'Test.SlErr(NO2)')


#%%

conc_df2.plot(x = 'Date_Time', y = 'Test.SlCol(O3)', yerr = 'Test.SlErr(O3)', linewidth = 0, marker = 'x') 

conc_df2.plot(x = 'Date_Time', y = 'Test.SlCol(NO2)',  yerr = 'Test.SlErr(NO2)')


#%%


#focussing on the stable section after 22:00

lower_lim = 1500
upper_lim = 3000


stable_Datetime = conc_df2['Date_Time'][lower_lim:upper_lim]
stable_SlCol_O3 = conc_df2['Test.SlCol(O3)'][lower_lim:upper_lim]
stable_SlErr_O3 = conc_df2['Test.SlErr(O3)'][lower_lim:upper_lim]
stable_SlCol_NO2 = conc_df2['Test.SlCol(NO2)'][lower_lim:upper_lim]
stable_SlErr_NO2 = conc_df2['Test.SlErr(NO2)'][lower_lim:upper_lim]



#%%

plt.plot(stable_Datetime, stable_SlCol_O3)
plt.title('SlCol(O3)')
plt.show()


plt.plot(stable_Datetime, stable_SlCol_NO2)
plt.title('SlCol(NO2)')
plt.show()


#%%

plt.errorbar(stable_Datetime, stable_SlCol_O3, yerr = stable_SlErr_O3, ecolor = 'red', elinewidth = 0.1, marker = '.', capsize = 1, markersize = 0.5)
plt.title('SlCol(O3)')
plt.xlabel('Date Time')
plt.ylabel('SlCol(O3)')
plt.show()

plt.errorbar(stable_Datetime, stable_SlCol_NO2, yerr = stable_SlErr_NO2, ecolor = 'red', elinewidth = 0.1, marker = '.', capsize = 1, markersize = 0.5)
plt.title('SlCol(NO2)')
plt.xlabel('Date Time')
plt.ylabel('SlCol(NO2)')
plt.show()


#%%























