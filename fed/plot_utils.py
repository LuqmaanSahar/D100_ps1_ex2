# This module creates plots of the GDP data

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
plt.style.use('seaborn-v0_8-whitegrid')

def plot_line(data: pd.DataFrame) -> Axes:
    """
    Creates a simple line plot using maplotlib

    Parameters
    ----------
    data: (pd.DataFrame) GDP dataset

    Returns
    ----------
    ax: (matplotlib.axes.Axes) matplotlib axis object for further customisation.
    """
    ax = data.plot(figsize=(10,6), kind="line", colormap='tab10')
    ax.set(title="GDP (Trillions USD) 2000–2022", ylabel="GDP (Trillions USD)",
            xlabel="Year")
    plt.legend(title="Country")

    return ax
