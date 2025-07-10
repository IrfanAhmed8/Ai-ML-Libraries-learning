import pandas as pd
import numpy as np


#load csv file for view purpose
df=pd.read_csv("complete.csv")


start_entries=df.head()
end_entries=df.tail()
column=df.columns
# to get the idea about the data.
#showed it contain 10 columns
print(start_entries)
print(end_entries)
print(column)



#now i will try to understand data through various function

print(df.shape)
#shape(4692,10)
print(df.info())
print(df.describe())
print(df['Name of State / UT'].value_counts())


print(df.isnull())
#deleting column named as latitude,longitude.
df.drop(columns=['Latitude', 'Longitude'], inplace=True)

state_data=df[df['Name of State / UT']=='Goa']
print(state_data)
print(state_data[['Date', 'New cases', 'New deaths']].tail())


state_wise=df.groupby('Name of State / UT')['New cases'].max().sort_values(ascending=False)
print(state_wise)

add_death_column=df['New cases']/df['New deaths']
print(add_death_column)

df['New cases']=np.where(df['New cases']> 40,'High','Low')

df.to_csv("newFile.csv",index=False)