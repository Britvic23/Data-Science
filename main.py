import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Count missions per year

missions_per_year = df['Launch Year'].value_counts().sort_index()



# Create a line plot

plt.figure(figsize=(12, 6))

sns.lineplot(x=missions_per_year.index, y=missions_per_year.values, marker='o')

plt.title('Number of Space Missions Launched Over Time (1957 onwards)')

plt.xlabel('Year')

plt.ylabel('Number of Missions')

plt.grid()

plt.show()

# Count the number of missions by type per year

mission_type_per_year = df.groupby(['Launch Year', 'Mission Type']).size().unstack().fillna(0)



# Create a stacked bar plot

mission_type_per_year.plot(kind='bar', stacked=True, figsize=(12, 6))

plt.title('Number of Missions by Type Over Time')

plt.xlabel('Year')

plt.ylabel('Number of Missions')

plt.legend(title='Mission Type')

plt.grid()

plt.show()

# Count missions per country

missions_per_country = df['Country'].value_counts()



# Create a bar plot for the top 10 countries

plt.figure(figsize=(12, 6))

sns.barplot(x=missions_per_country.head(10).index, y=missions_per_country.head(10).values)

plt.title('Top 10 Countries by Number of Space Missions')

plt.xlabel('Country')

plt.ylabel('Number of Missions')

plt.xticks(rotation=45)

plt.grid()

plt.show()

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns



# Load the dataset

df = pd.read_csv('path_to_your_space_mission_data.csv')



# Clean the data

df.dropna(inplace=True)

df['Launch Year'] = pd.to_datetime(df['Launch Year'], format='%Y').dt.year



# Count missions per year

missions_per_year = df['Launch Year'].value_counts().sort_index()



# Create a line plot for missions per year

plt.figure(figsize=(12, 6))

sns.lineplot(x=missions_per_year.index, y=missions_per_year.values, marker='o')

plt.title('Number of Space Missions Launched Over Time (1957 onwards)')

plt.xlabel('Year')

plt.ylabel('Number of Missions')

plt.grid()

plt.show()



# Count the number of missions by type per year

mission_type_per_year = df.groupby(['Launch Year', 'Mission Type']).size().unstack().fillna(0)



# Create a stacked bar plot for mission types

mission_type_per_year.plot(kind='bar', stacked=True, figsize=(12, 6))

plt.title('Number of Missions by Type Over Time')

plt.xlabel('Year')

plt.ylabel('Number of Missions')

plt.legend(title='Mission Type')

plt.grid()

plt.show()



# Count missions per country

missions_per_country = df['Country'].value_counts()



# Create a bar plot for the top 10 countries

plt.figure(figsize=(12, 6))

sns.barplot(x=missions_per_country.head(10).index, y=missions_per_country.head(10).values)

plt.title('Top 10 Countries by Number of Space Missions')

plt.xlabel('Country')

plt.ylabel('Number of Missions')

plt.xticks(rotation=45)

plt.grid()

plt.show()