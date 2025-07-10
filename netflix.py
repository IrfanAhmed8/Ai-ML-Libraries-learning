import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("netflix.csv")
start=df.head()

info=df.info()




type_movies=df['type'].value_counts()
print(type_movies)
country_data=df['country'].value_counts()
print(country_data)
#filter_indices=np.where(country_data.values>50)[0]
filter_countries=country_data[country_data>50]
#print(filter_indices)
print(filter_countries)


plt.figure(figsize=(7,10))
plt.barh(filter_countries.index,filter_countries,color='mediumseagreen')
plt.title("Countries with More Than 50 Netflix Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


plt.figure(figsize=(7,4))
plt.bar(type_movies.index,type_movies.values,color=['tomato', 'skyblue'])
plt.title("Distribution of Content Type on Netflix")
plt.xlabel("Type of Content")
plt.ylabel("Number of Titles")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()





