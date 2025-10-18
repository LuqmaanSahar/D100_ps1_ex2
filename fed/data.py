# This module will load annual GDP data for different countries

import pandas as pd
import pandas_datareader.wb as wb

countries = ['GB', 'US', 'BR', 'JP', 'CN', 'DE', 'CH']
indicator = 'NY.GDP.MKTP.CD'
start_year = 2000
end_year = 2022


def data_load(units = 1e12, countries=countries, indicator=indicator, 
              start=start_year, end=end_year):
    """
    loads GDP data from World Bank

    Parameters
    ----------
    units: (float) data units in US$
    countries: (list) list of country codes to download data for
    indicator: (str) Dataset to download. Default is annual GDP in current US$
    start: (int) start year of time series
    end: (int) end year of time series

    Returns
    ----------
    data: (DataFrame) the tidy dataset
    """
    data = wb.download(indicator=indicator,
                country=countries,
                start=start,
                end=end
            ).reset_index().pivot(index='year', columns='country', values='NY.GDP.MKTP.CD')
    data=data/units
    
    return data
