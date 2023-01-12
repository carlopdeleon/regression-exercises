import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pydataset import data
from scipy import stats
from env import host, username, password    # import needed for get_connection() to operate


# Function to build the connection between notebook and MySql. Will be used in other functions.
# Returns the string that is neccessary for that connection.
def get_connection(db, user = username, host = host, password = password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def get_zillow():
    filename = "zillow.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql("select bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount,\
             fips from properties_2017 join propertylandusetype using(propertylandusetypeid) where propertylandusedesc = \
                'Single Family Residential'", get_connection('zillow'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename, index=False)

        # Return the dataframe
        return df  
    


    

def clean_zillow(zillow):

# Dropped all nulls. Less than 1% of data.
    zillow = zillow.dropna()

    return zillow





def wrangle_zillow():

    #Acquire Zillow data
    zillow = get_zillow()
    # Drop the nulls. Less than 1% of the data
    zillow = zillow.dropna()

    return zillow
    

