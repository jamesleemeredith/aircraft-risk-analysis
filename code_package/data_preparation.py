"""
## DATA CLEANING MODULE
Data source: https://www.kaggle.com/datasets/khsamaha/aviation-accident-database-synopses

This module cleans the data in preperation for analysis

"""
import pandas as pd

def column_cleaning(aviation_raw):
    """Cleans aviation data"""
    # Assign to variable for cleaning
    aviation_data_cleaned = aviation_raw
    # Strip out extra spaces
    aviation_data_cleaned.columns = aviation_data_cleaned.columns.str.strip()
    # Replace . with _
    aviation_data_cleaned.columns = aviation_data_cleaned.columns.str.replace(".","_")
    # Lowercase all names
    aviation_data_cleaned.columns = aviation_data_cleaned.columns.str.lower()
    
    # Drop duplicates
    aviation_data_cleaned = aviation_data_cleaned.drop_duplicates()
    # Drip duplicate events but keep the first reported event
    aviation_data_cleaned = aviation_data_cleaned.drop_duplicates(subset=['event_id'], keep='first')
    
    # Including data only from the USA
    usa_filter = aviation_data_cleaned['country'] == 'United States'
    aviation_data_cleaned = aviation_data_cleaned[usa_filter]
    # Drop the country column since there is now only one value
    aviation_data_cleaned = aviation_data_cleaned.drop('country', axis=1)
    
    # We don't want any amateur built airplanes so let's remove the data 
    pro_filter = aviation_data_cleaned['amateur_built'] == 'No'
    aviation_data_cleaned = aviation_data_cleaned[pro_filter]
    # Now drop the amateur_built column since all remaining aircraft are professionally built
    aviation_data_cleaned = aviation_data_cleaned.drop('amateur_built', axis=1)
    
    # Update the column to the correct datetime type
    aviation_data_cleaned['event_date'] = pd.to_datetime(aviation_data_cleaned['event_date'])
    
    # There are only a few datapoints before 1082 so let's remove them
    aviation_data_cleaned = aviation_data_cleaned[aviation_data_cleaned['event_date'].dt.year >= 1982]
    
    # Drop columns with irrelevant data
    aviation_data_cleaned = aviation_data_cleaned.drop([
    'accident_number',
    'registration_number',
    'publication_date',
    'investigation_type'
    ], axis=1)
    
    # Pull out columns to drop with over 60% missing data
    missing_data = (aviation_data_cleaned.isna().sum() / len(aviation_data_cleaned)).sort_values(ascending=False)
    columns_to_drop = missing_data[missing_data.values > 0.6].index.to_list()
    aviation_data_cleaned = aviation_data_cleaned.drop(columns_to_drop, axis=1)

    return aviation_data_cleaned

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
    aviation_data_cleaned = column_cleaning(aviation_raw)
    # aviation_clean.to_csv('data/Aviation_Data_Cleaned.csv')
    
    return aviation_data_cleaned