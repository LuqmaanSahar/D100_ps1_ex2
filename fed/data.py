# This module will load annual GDP data for different countries

import pandas as pd
import pandas_datareader.wb as wb
from typing import cast

countries = ['GB', 'US', 'BR', 'JP', 'CN', 'DE', 'CH']
indicator = 'NY.GDP.MKTP.CD'
start_year = 2000
end_year = 2022


def data_load(
    units: float = 1e12,
    countries: list[str] = countries,
    indicator: str = indicator,
    start: int = start_year,
    end: int = end_year
    ) -> pd.DataFrame:
    """
    loads GDP data from World Bank

    Parameters
    ----------
    units: (float) data units in US$
    countries: (list[str]) list of country codes to download data for
    indicator: (str) Dataset to download. Default is annual GDP in current US$
    start: (int) start year of time series
    end: (int) end year of time series

    Returns
    ----------
    data: (pd.DataFrame) the tidy dataset
    """
    data = wb.download(indicator=indicator,
                country=countries,
                start=start,
                end=end
            ).reset_index().pivot(index='year', columns='country', values='NY.GDP.MKTP.CD')
    data=cast(pd.DataFrame, data/units)

    return data # type: ignore[no-any-return]

# could also use pd.melt() instead of pd.pivot() if we wanted year as a variable, not as an index.
# pd.melt(var_name='year', id_vars='country', value_name='NY.GDP.MKTP.CD')
