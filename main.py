import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
from tabulate import tabulate
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('WHO-COVID-19-global-data.csv')
#print(df.head(10))

#print(df.describe(include='all'))

df['Date_reported'] = pd.to_datetime(df['Date_reported'], errors='coerce')

df['year'] = df['Date_reported'].dt.year

df.drop(['Country_code','Date_reported'],axis=1,inplace=True)

#print(df['Country'].unique())

covid_Cumulative_cases = pd.DataFrame(df.groupby("Country")['Cumulative_cases']
                               .agg('sum')).sort_values(by='Cumulative_cases',ascending=False,axis=0)

#print(covid_Cumulative_cases.head())

covid_Cumulative_cases.head(10).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of Cumulative cases (Millions)',title = 'Cumulative Covid19 Cases')
plt.show()

covid_Cumulative_least_cases = pd.DataFrame(df.groupby("Country")['Cumulative_cases']
                               .agg('sum')).sort_values(by='Cumulative_cases',ascending=True,axis=0)


covid_Cumulative_least_cases.head(10).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of Cumulative cases (Millions)',title = 'No of Cumulative cases')
plt.show()


covid_new_cases = pd.DataFrame(df.groupby("Country")['New_cases']
                               .agg('sum')).sort_values(by='New_cases',ascending=False,axis=0)

covid_new_cases.head(10).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of New_cases',title = 'New Covid19 cases Recorded', figsize=(15,10))
plt.show()

covid_least_new_cases = pd.DataFrame(df.groupby("Country")['New_cases']
                               .agg('sum')).sort_values(by='New_cases',ascending=True,axis=0)


covid_least_new_cases.head(10).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of New_cases',title = 'New Covid19 cases Recorded', figsize=(15,10))
plt.show()


covid_new_death = pd.DataFrame(df.groupby("Country")['New_deaths']
                               .agg('sum')).sort_values(by='New_deaths',ascending=False,axis=0)

covid_new_death.head(10).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of New_Death',title = 'Total of Number of deaths')
plt.show()


covid_new_least_death = pd.DataFrame(df.groupby("Country")['New_deaths']
                               .agg('sum')).sort_values(by='New_deaths',ascending=True,axis=0)


covid_new_least_death.head(10).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of New_Death',title = 'Total of Number of deaths')
plt.show()


covid_Cumulative_deaths = pd.DataFrame(df.groupby("Country")['Cumulative_deaths']
                               .agg('sum')).sort_values(by='Cumulative_deaths',ascending=False,axis=0)

covid_Cumulative_deaths.head(15).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of Cumulative death',title = 'No of Cumulative deaths')
plt.show()

covid_Cumulative_least_deaths = pd.DataFrame(df.groupby("Country")['Cumulative_deaths']
                               .agg('sum')).sort_values(by='Cumulative_deaths',ascending=True,axis=0)

covid_Cumulative_least_deaths.head(15).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of Cumulative death',title = 'Cumulative deaths')
plt.show()


covid_cum_new_year = pd.DataFrame(df.groupby(["Country",'year'])['Cumulative_cases']
                               .agg('sum')).sort_values(by=['year', 'Cumulative_cases'],ascending=False,axis=0)


covid_cum_new_year = pd.DataFrame(df.groupby(["Country",'year'])['Cumulative_cases']
                               .agg('sum')).sort_values(by=['year', 'Cumulative_cases'],ascending=True,axis=0)


covid_New_cases_year = pd.DataFrame(df.groupby(["Country",'year'])['New_cases']
                               .agg('sum')).sort_values(by=['year', 'New_cases'],ascending=False,axis=0)

covid_New_cases_year = pd.DataFrame(df.groupby(["Country",'year'])['New_cases']
                               .agg('sum')).sort_values(by=['year', 'New_cases'],ascending=True,axis=0)

covid_cum_death_cases_year = pd.DataFrame(df.groupby(["Country",'year'])['Cumulative_deaths']
                               .agg('sum')).sort_values(by=['year', 'Cumulative_deaths'],ascending=False,axis=0)


covid_new_death_cases_year = pd.DataFrame(df.groupby(["Country",'year'])['New_deaths']
                               .agg('sum')).sort_values(by=['year', 'New_deaths'],ascending=False,axis=0)

cases_2020 = df[df['year']== 2020]

covid_New_cases_year_cases_2020 = pd.DataFrame(cases_2020.groupby(["Country",'year'])['New_cases']
                               .agg('sum')).sort_values(by=['year', 'New_cases'],ascending=False,axis=0)


covid_New_cases_year_cases_2020 = pd.DataFrame(cases_2020.groupby(["Country",'year'])['New_cases']
                               .agg('sum')).sort_values(by=['year', 'New_cases'],ascending=True,axis=0)


cases_2021 = df[df['year']== 2021]

covid_New_cases_year_cases_2021 = pd.DataFrame(cases_2021.groupby(["Country",'year'])['New_cases']
                               .agg('sum')).sort_values(by=['year', 'New_cases'],ascending=False,axis=0)


covid_New_cases_year_cases_2021 = pd.DataFrame(cases_2021.groupby(["Country",'year'])['New_cases']
                               .agg('sum')).sort_values(by=['year', 'New_cases'],ascending=True,axis=0)

cases_2022 = df[df['year']== 2022]

covid_New_cases_year_cases_2022 = pd.DataFrame(cases_2022.groupby(["Country",'year'])['New_cases']
                               .agg('sum')).sort_values(by=['year', 'New_cases'],ascending=False,axis=0)

covid_New_cases_year_cases_2022 = pd.DataFrame(cases_2022.groupby(["Country",'year'])['New_cases']
                               .agg('sum')).sort_values(by=['year', 'New_cases'],ascending=True,axis=0)


covid_region_Cumulative_deaths = pd.DataFrame(df.groupby("WHO_region")['Cumulative_deaths']
                               .agg('sum')).sort_values(by='Cumulative_deaths',ascending=False,axis=0)


covid_region_New_deaths = pd.DataFrame(df.groupby("WHO_region")['New_deaths']
                               .agg('sum')).sort_values(by='New_deaths',ascending=False,axis=0)


covid_region_Cumulative_cases = pd.DataFrame(df.groupby("WHO_region")['Cumulative_cases']
                               .agg('sum')).sort_values(by='Cumulative_cases',ascending=False,axis=0)



covid_region_New_cases = pd.DataFrame(df.groupby("WHO_region")['New_cases']
                               .agg('sum')).sort_values(by='New_cases',ascending=False,axis=0)

Covid_19 = df

africa_cases= Covid_19[Covid_19['WHO_region'] =='AFRO']

top_countries = pd.DataFrame(africa_cases.groupby("Country")['Cumulative_cases']
                               .agg('sum')).sort_values(by='Cumulative_cases',ascending=False,axis=0)


top_countries.head(10).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of Cumulative cases',title = 'Cumulative cases')
plt.show()


top_countries.head(10).unstack(level=0).plot(
    kind='pie',
    stacked=True,
    subplots=True,
    autopct='%1.1f%%',
    figsize=(10, 10),
    legend=False,
    )
plt.show()


africa_cases= Covid_19[Covid_19['WHO_region']=='AFRO']

africa_cases['Cumulative_cases'].sum()

print('Africa has a total cumulative cases of about', africa_cases['Cumulative_cases'].sum()) 

africa_death_cases=Covid_19[Covid_19['WHO_region']=='AFRO']
africa_death_cases=pd.DataFrame(africa_death_cases.groupby("Country")['Cumulative_deaths']
                               .agg('sum')).sort_values(by='Cumulative_deaths',ascending=False,axis=0)

africa_death_cases.head(10).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of Cumulative death',title = 'Top ten death cases in Africa')
plt.show()

africa_death_cases.head(10).unstack(level=0).plot(
    kind='pie',
    stacked=True,
    subplots=True,
    autopct='%1.1f%%',
    figsize=(10, 10),
    legend=False,
    )
plt.show()

africa_death_cases=Covid_19[Covid_19['WHO_region']=='AFRO']



america_cases= Covid_19[Covid_19['WHO_region']=='AMRO']

america_cases = pd.DataFrame(america_cases.groupby("Country")['Cumulative_cases']
                               .agg('sum')).sort_values(by='Cumulative_cases',ascending=False,axis=0)

america_cases.head(10).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of Cumulative caes',title = 'Top ten affected countries(AMRO)')
plt.show()


america_cases.head(10).unstack(level=0).plot(
    kind='pie',
    stacked=True,
    subplots=True,
    autopct='%1.1f%%',
    figsize=(10, 10),
    legend=False,
    )
plt.show()


america_cases= Covid_19[Covid_19['WHO_region']=='AMRO']

america_death_cases=Covid_19[Covid_19['WHO_region']=='AMRO']


america_death_cases = pd.DataFrame(america_death_cases.groupby("Country")['Cumulative_deaths']
                               .agg('sum')).sort_values(by='Cumulative_deaths',ascending=False,axis=0)



america_death_cases.head(10).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of Cumulative death',title = 'Top ten affected countries(AMRO)')
plt.show()

america_death_cases.head(10).unstack(level=0).plot(
    kind='pie',
    stacked=True,
    subplots=True,
    autopct='%1.1f%%',
    figsize=(10, 10),
    legend=False,
    )
plt.show()


southeast_cases= Covid_19[Covid_19['WHO_region']=='SEARO']

southeast_cases = pd.DataFrame(southeast_cases.groupby("Country")['Cumulative_cases']
                               .agg('sum')).sort_values(by='Cumulative_cases',ascending=False,axis=0)

southeast_cases.head(10).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of Cumulative cases',title = 'Top ten affected countries(SEARO)')
plt.show()



southeast_cases.head(8).unstack(level=0).plot(
    kind='pie',
    stacked=True,
    subplots=True,
    autopct='%1.1f%%',
    figsize=(15, 10),
    legend=False,
    )
plt.show()

southeast_cases= Covid_19[Covid_19['WHO_region']=='SEARO']

southeast_death_cases=Covid_19[Covid_19['WHO_region']=='SEARO']
southeast_death_cases = pd.DataFrame(southeast_death_cases.groupby("Country")['Cumulative_deaths']
                               .agg('sum')).sort_values(by='Cumulative_deaths',ascending=False,axis=0)

southeast_death_cases.head(10).plot(kind='bar',  xlabel = 'Country', ylabel = 'No. of Cumulative deaths',title = 'Top ten affected countries(SEARO)')
plt.show()

southeast_death_cases.head(5).unstack(level=0).plot(
    kind='pie',
    stacked=True,
    subplots=True,
    autopct='%1.1f%%',
    figsize=(15, 10),
    legend=False,
    )
plt.show()

southeast_death_cases= Covid_19[Covid_19['WHO_region']=='SEARO']
