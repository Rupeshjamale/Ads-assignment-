# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:24:54 2022

@author: Rupesh
"""

import pandas as pd #for importing pandas
import numpy as np #for importing numpy
import matplotlib.pyplot as plt #for importing matplotlib
import scipy.stats as stats #for scipy


def getdata(filename):
    '''
    This fuction returns two dataframes.One with years as column and other with countries as column
    we have transposed data from row to column as well as column to rows.
    It takes one argument as file name to read the data using pandas.
    
    '''
    df = pd.read_csv(filename, skiprows=(4), index_col=False) #for reading csv file and skipping unused rows from data
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #for dropping column from data
    df = df.loc[df['Country Name'].isin(countries)]#for selecting specific column from data
    df2 = df.melt(id_vars=['Country Name','Country Code','Indicator Name','Indicator Code'], var_name='Years') # Converting years in a single column 
    del df2['Country Code'] # Deleting coutry code column
    df2 = df2.pivot_table('value',['Years','Indicator Name','Indicator Code'],'Country Name').reset_index() # Creating countries separate columns from rows.
    return df, df2 # Returning two dataframes one with countries as column and other with years as column


countries = ['Finland','Belgium','Switzerland','Germany'] # Countries list to filter data

#------------------------------------------------------------------------------
#Lineplot for Electric power consumption (kWh per capita)
#------------------------------------------------------------------------------
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv') # reading file to dataframes using defined function.
df2 = df2.loc[df2['Indicator Code'].eq('EG.USE.ELEC.KH.PC')] # Filter data using indicator code.

# Plotting data 
plt.figure()
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title='Electric power consumption (kWh per capita)')
plt.xlim(1990,2014)
plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.show()


#--------------------------------------------------------------------------------------------------
# Piechart for Electricity production from renewable sources, excluding hydroelectric (% of total)
#--------------------------------------------------------------------------------------------------
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv') # reading file to dataframes using defined function.
df2 = df2.loc[df2['Indicator Code'].eq('EG.ELC.RNWX.ZS')] # Filter data using indicator code.

# Creating data to show on pie chart
fin= np.sum(df2['Finland'])
bel= np.sum(df2['Belgium'])
swi= np.sum(df2['Switzerland'])
ger= np.sum(df2["Germany"])

total= fin + bel  + swi + ger

fin_eu = fin/ total*100
bel_eu = bel/ total*100
swi_eu = swi/ total*100
ger_eu = ger/ total*100

Energy_use= np.array([fin_eu, bel_eu,swi_eu, ger_eu])
# Plotting data on pie chart
plt.figure(dpi=144)
plt.pie(Energy_use, labels= countries, shadow=True, autopct=('%1.1f%%'))# We used autopct for showing percantages on piechart
plt.title("Electricity production from renewable sources, excluding hydroelectric (% of total)") # This function is for showing title of data
plt.show()
        
#Read the file into dataframes.
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv') # reading file to dataframes using defined function.
df2 = df2.loc[df2['Indicator Code'].eq('EG.USE.COMM.GD.PP.KD')] # Filter data using indicator code.
df2 = df2.loc[df2['Years'].isin(['2015'])]

#Statatical function return the mean of the co2 emission of the country.
df2_min = df2[["Finland","Switzerland","Belgium","Germany"]].min()
print(df2_min)
df2_skew = stats.skew(df2[countries])
print(df2_skew)

#converting the data to csv file
df2 = df2.to_csv("mean.csv")
 
#------------------------------------------------------------------------------
#Barplot for Access to electricity (% of population)
#------------------------------------------------------------------------------
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv') # reading file to dataframes using defined function.
df2 = df2.loc[df2['Indicator Code'].eq('EG.FEC.RNEW.ZS')] # Filter data using indicator code.

df2 = df2.loc[df2['Years'].isin(['2000','2001','2002','2003','2004'])]
num = np.arange(5)
width = 0.2
years = df2['Years'].tolist()

plt.figure(dpi=120)
plt.title('Access to electricity (% of population)')
plt.bar(num, df2['Finland'], width, label='Finland')
plt.bar(num+0.2, df2['Belgium'], width, label='Belgium')
plt.bar(num+0.4, df2['Switzerland'], width, label='Switzerland')
plt.bar(num-0.2, df2['Germany'], width, label='Germany')
plt.xticks(num, years)
plt.xlabel('Years')
plt.ylabel('% Of Population')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5)) # to show legends outside of the box
plt.show()

#------------------------------------------------------------------------------
# new one Line plot2
#------------------------------------------------------------------------------
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv') # reading file to dataframes using defined function.
df2 = df2.loc[df2['Indicator Code'].eq('EG.ELC.RNEW.ZS')] # Filter data using indicator code.

plt.figure()
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title='Renewable electricity output (% of total electricity output)')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.show()

#------------------------------------------------------------------------------
# new pie chart2 for Electricity production from hydroelectric sources (% of total)
#------------------------------------------------------------------------------
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv') # reading file to dataframes using defined function.
df2 = df2.loc[df2['Indicator Code'].eq('EG.ELC.HYRO.ZS')] # Filter data using indicator code.
# calculating data for pie chart
fin = np.sum(df2['Finland'])
bel = np.sum(df2['Belgium'])
swi = np.sum(df2['Switzerland'])
ger = np.sum(df2["Germany"])
total= fin + bel + swi + ger

fin_eu = fin/ total*100
bel_eu = bel/ total*100
swi_eu = swi/ total*100
ger_eu = ger/ total*100

Energy_use= np.array([fin_eu, bel_eu,swi_eu, ger_eu])


plt.figure(dpi=144)
plt.pie(Energy_use, labels= countries, shadow=True, autopct=('%1.1f%%'))# We used autopct for showing percantages on piechart
plt.title("Electricity production from hydroelectric sources (% of total)") # This function is for showing title of data
plt.show()

#------------------------------------------------------------------------------
#bar plot2 for Population, total
#------------------------------------------------------------------------------
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv') # reading file to dataframes using defined function.
df2 = df2.loc[df2['Indicator Code'].eq('SP.POP.TOTL')] # Filter data using indicator code.

df2 = df2.loc[df2['Years'].isin(['2000','2001','2002','2003','2004'])] # Selecting years data
num = np.arange(5)
width = 0.2 # defining width of bar for the barchart
years = df2['Years'].tolist() # Years to show on x-axis
# Plotting data on bar plot grouped
plt.figure(dpi=120)
plt.title('Population, total')
plt.bar(num, df2['Finland'], width, label='Finland')
plt.bar(num+0.2, df2['Belgium'], width, label='Belgium')
plt.bar(num+0.4, df2['Switzerland'], width, label='Switzerland')
plt.bar(num-0.2, df2['Germany'], width, label='Germany')
plt.xticks(num, years)
plt.xlabel('Years')
plt.ylabel('% Of Population')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5)) # To show legends outside of the box
plt.show()





