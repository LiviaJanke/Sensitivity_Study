# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:32:30 2023

@author: lme19
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%

test1_df = pd.read_csv('polynom_order_2_with_CLD.ASC', skiprows = 8, delimiter = '\t')
#no_I0_df = pd.read_csv('test_425_465_no_I0_v2.ASC', skiprows = 8, delimiter = '\t')

#no_CLD_df = pd.read_csv('test_pseudoabsorbers_interpolated.ASC', skiprows = 8, delimiter = '\t')

#%%

test1_df.plot()

date_and_time = test1_df['# Date (DD/MM/YYYY)'] + ' ' + test1_df['Time (hh:mm:ss)']

datetime = pd.to_datetime(test1_df['# Date (DD/MM/YYYY)'] + ' ' + test1_df['Time (hh:mm:ss)'])


#date_time_no_I0 = no_I0_df['# Date (DD/MM/YYYY)'] + ' ' + no_I0_df['Time (hh:mm:ss)']

#datetime_no_I0 = pd.to_datetime(no_I0_df['# Date (DD/MM/YYYY)'] + ' ' + no_I0_df['Time (hh:mm:ss)'])

#%%

plt.plot(datetime, test1_df['Test.SlCol(O3)'])
plt.show()

test1_df['Date_Time'] = datetime
#no_I0_df['Date_Time_no_I0'] = datetime_no_I0

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
#conc_non_CLD = no_CLD_df.drop(columns =['# Date (DD/MM/YYYY)', 'Time (hh:mm:ss)', 'Scans', 'Longitude', 'Latitude'])

corrected_df = test1_df.drop([2368])
conc_df2 = conc_df.drop([2368])

#corrected_non_CLD = no_CLD_df.drop([2360])
#conc_non_CLD_2 = conc_non_CLD.drop([2360])

#corrected_df_no_I0 = no_I0_df.drop([2368])

#%%
corrected_df.plot(x = 'Date_Time')

#%%
conc_df2.plot(x = 'Date_Time')

#%%

conc_df2.plot(x = 'Date_Time', y = 'Test.SlCol(O3)', yerr = 'Test.SlErr(O3)', linewidth = 0, marker = '.') 

conc_df2.plot(x = 'Date_Time', y = 'Test.SlCol(NO2)',  yerr = 'Test.SlErr(NO2)')


#%%

conc_df2.plot(x = 'Date_Time', y = 'Test.SlCol(O3)', yerr = 'Test.SlErr(O3)', linewidth = 0, marker = '.') 

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

#stable_Datetime_no_CLD = conc_non_CLD_2['Date_Time'][lower_lim:upper_lim]
#stable_SlCol_O3_no_CLD = conc_non_CLD_2['Test.SlCol(O3)'][lower_lim:upper_lim]
#stable_SlErr_O3_no_CLD = conc_non_CLD_2['Test.SlErr(O3)'][lower_lim:upper_lim]
#stable_SlCol_NO2_no_CLD = conc_non_CLD_2['Test.SlCol(NO2)'][lower_lim:upper_lim]
#stable_SlErr_NO2_no_CLD = conc_non_CLD_2['Test.SlErr(NO2)'][lower_lim:upper_lim]

#stable_Datetime_no_I0 = corrected_df_no_I0['Date_Time_no_I0'][lower_lim:upper_lim]
#stable_SlCol_O3_no_I0 = corrected_df_no_I0['Test.SlCol(O3)'][lower_lim:upper_lim]
#stable_SlErr_O3_no_I0 = corrected_df_no_I0['Test.SlErr(O3)'][lower_lim:upper_lim]
#stable_SlCol_NO2_no_I0 = corrected_df_no_I0['Test.SlCol(NO2)'][lower_lim:upper_lim]
#stable_SlErr_NO2_no_I0 = corrected_df_no_I0['Test.SlErr(NO2)'][lower_lim:upper_lim]


#%%

plt.plot(stable_Datetime, stable_SlCol_O3)
plt.title('SlCol(O3)')
plt.show()


plt.plot(stable_Datetime, stable_SlCol_NO2)
plt.title('SlCol(NO2)')
plt.show()


#%%

plt.errorbar(stable_Datetime, stable_SlCol_O3, yerr = stable_SlErr_O3, linewidth = 0, ecolor = 'red', elinewidth = 0.1, marker = '.', color = 'red', capsize = 1, markersize = 0.5)
plt.title('SlCol(O3)')
plt.xlabel('Date Time')
plt.ylabel('SlCol(O3)')

#plt.errorbar(stable_Datetime_no_I0, stable_SlCol_O3_no_I0, yerr = stable_SlErr_O3_no_I0, linewidth = 0, ecolor = 'black', elinewidth = 0.1, marker = 'x', capsize = 1, markersize = 0.5, color = 'black', label = 'No I0 correction')
plt.legend()
plt.show()


#%%

plt.errorbar(stable_Datetime, stable_SlCol_NO2, yerr = stable_SlErr_NO2, linewidth = 0, ecolor = 'red', elinewidth = 0.1, marker = '.', capsize = 1, markersize = 0.5, color = 'red')

#plt.errorbar(stable_Datetime_no_I0, stable_SlCol_NO2_no_I0, yerr = stable_SlErr_NO2_no_I0, linewidth = 1, ecolor = 'black', elinewidth = 0.1, marker = 'X', capsize = 1, markersize = 0.5, color = 'black', label = 'No I0 correction')
plt.title('SlCol(NO2)')
plt.xlabel('Date Time')
plt.ylabel('SlCol(NO2)')
plt.legend()
plt.show()


#%%























