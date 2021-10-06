import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from vega_datasets import data
import numpy as np
from acquire import merge_data, germany_df
from datetime import timedelta, datetime



def store_prep(df = merge_data()):
    '''
        prep is taking in a dataframe dropping the index column, making date as 
        the index.  It is also making three new columns month, day_of_week, and sales_total
    
    '''
    
    # Converting sale_date type object to datetime64
    df.sale_date = pd.to_datetime(df.sale_date.apply(lambda x: x[:-13]))

    # Making the index equal to the sale_date
    df = df.set_index('sale_date').sort_index()
    
    # Creating a column named month and using sale_date.dt.month to extract just the month
    df['month'] = pd.DatetimeIndex(df.index).month
    
    # Creating a column named month and using sale_date.dt.month to extract just the month
    df['day_of_week'] = pd.DatetimeIndex(df.index).day_name()
    
    # Multiplying sales_amount by item price. Saving as sales_total
    df['sales_total'] = df['sale_amount'] * df['item_price']
    
    return df


def prep_opsd(df = germany_df()):
    '''
        Preps the german OPSD df by removing nulls and creating a column wind + solar
    '''
    # Converting Date type object to datetime64
    df.Date = pd.to_datetime(df.Date)
    
    # Making the index equal to the Date column
    df = df.set_index('Date').sort_index()
    
    # Creating a column named month
    df['month'] = pd.DatetimeIndex(df.index).month
    
    # Creating a column named year
    df['year'] = pd.DatetimeIndex(df.index).year
    
    # Fill nans
    df = df.fillna(0)
    
    # Replacing faulty wind+solar
    df = df.drop(columns = ['Wind+Solar'])
    df['Wind_Solar'] = df['Wind'] + df['Solar']
    
    return df