import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("netflix.csv")
start=df.head()

info=df.info()




type_movies=df['type'].value_counts()
#print(type_movies)
country_data=df['country'].value_counts()
#print(country_data)
#filter_indices=np.where(country_data.values>50)[0]
filter_countries=country_data[country_data>50]
#print(filter_indices)
#print(filter_countries)

print(info)
# years wise shows detail
df['date_added'] = df['date_added'].str.strip()
#convert date into perfect format
df['date_added']=pd.to_datetime(df['date_added'])
df['year_added']=df['date_added'].dt.year

movies_year=df['year_added'].value_counts()
print(movies_year)

# Create a single canvas with 3 vertically stacked subplots
import matplotlib.pyplot as plt

# Plot 1: Country Chart
plt.figure(figsize=(10, 6))
plt.barh(filter_countries.index, filter_countries, color='mediumseagreen')
plt.title("Countries with More Than 50 Netflix Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("countries_plot.png")  # ✅ Save to file
plt.close()

# Plot 2: Type of Content
plt.figure(figsize=(6, 4))
plt.bar(type_movies.index, type_movies.values, color=['tomato', 'skyblue'])
plt.title("Distribution of Content Type on Netflix")
plt.xlabel("Type of Content")
plt.ylabel("Number of Titles")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("type_distribution.png")
plt.close()

# Plot 3: Movies Per Year
plt.figure(figsize=(10, 6))
plt.bar(movies_year.index, movies_year.values, color='red')
plt.title("Movies Added Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("movies_per_year.png")
plt.close()
