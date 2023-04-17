"""
## DATA CLEANING MODULE
Data source: https://www.kaggle.com/datasets/khsamaha/aviation-accident-database-synopses

This module cleans the data in preperation for analysis

"""
import pandas as pd

def cleaning_aviation_data(aviation_raw):
    """Cleans aviation data"""
    return aviation_clean

def full_clean():
    """
    Main cleaning function that will call support functions
    Assumption: 
        - Your data files will be saved in a data folder and named "Aviation_Data.csv"
    -
    Input:
    df : Pandas dataframe
    -
    Output:
    summary : Pandas dataframe, cleaned and ready for anaysis
    """
    aviation_raw = pd.read_csv("data/Aviation_Data.csv")
    aviation_clean = cleaning_aviation_data(aviation_raw)
    aviation_clean.to_csv('data/Aviation_Data_Cleaned.csv')
    
    return cleaned_data