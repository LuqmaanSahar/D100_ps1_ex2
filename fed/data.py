# This module will load annual GDP data for different countries

import pandas as pd
import pandas_datareader.wb as wb

countries = ['GB', 'US', 'BR', 'JP', 'CN', 'DE', 'CH']
indicator = 'NY.GDP.MKTP.CD'
start_year = 2000
end_year = 2022


def data_load(units = 1e12, countries=countries, indicator=indicator, 
              start=start_year, end=end_year):

    data = wb.download(indicator=indicator,
                country=countries,
                start=start,
                end=end
            ).reset_index().pivot(index='year', columns='country', values='NY.GDP.MKTP.CD')
    data=data/units
    
    return data
