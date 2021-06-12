import numpy as np
import pandas as pd


def table_1() -> pd.DataFrame:
    """Load table 1. It returns a Pandas DataFrame"""
    # load the data
    table1 = pd.read_csv('./data/Covid_deaths.csv')
    t_1 = table1.copy()
    # Drop missing values
    t_1 = t_1.dropna(subset=['continent'])
    cols = ['population', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']
    # replace missing values with '0'
    for col in cols:
        t_1[col] = np.where(pd.isna(t_1[col]) == True, 0, t_1[col])
    # replace missing values with 'NULL'
    for col in ['iso_code', 'continent', 'location']:
        t_1[col] = np.where(pd.isna(t_1[col]) == True, 'NULL', t_1[col])         
    # convert to the appropriate data types
    for col in cols:
        t_1[col] = t_1[col].apply(lambda x: int(x))  
    # convert to datetime
    t_1['date'] = pd.to_datetime(t_1['date'])
    return t_1

def table_2() -> pd.DataFrame:
    """Load table 2. It returns a Pandas DataFrame"""
    table2 = pd.read_csv('./data/Covid_Vaccinations.csv')
    t_2 = table2.copy()
    # Drop missing values
    t_2 = t_2.dropna(subset=['continent'])
    cols = ['new_tests', 'total_tests', 'positive_rate', 'tests_per_case', 'tests_units', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
        'new_vaccinations', 'stringency_index', 'population_density', 'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita',
        'handwashing_facilities', 'hospital_beds_per_thousand', 'life_expectancy', 'human_development_index'] 

    # replace missing values with '0'
    for col in cols:
        t_2[col] = np.where(pd.isna(t_2[col]) == True, 0, t_2[col])
    # replace missing values with 'NULL'
    for col in ['iso_code', 'continent', 'location']:
        t_2[col] = np.where(pd.isna(t_2[col]) == True, 'NULL', t_2[col])            
    # convert to the appropriate data types
    for col in ['new_tests', 'total_tests', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'new_vaccinations',]:
        t_2[col] = t_2[col].apply(lambda x: int(x))  
    # convert to datetime
    t_2['date'] = pd.to_datetime(t_2['date'])
    return t_2
   