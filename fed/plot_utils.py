# This module creates plots of the GDP data

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')

def plot_line(data):
    ax = data.plot(figsize=(10,6), kind="line", colormap='tab10')
    ax.set(title="GDP (Trillions USD) 2000–2022", ylabel="GDP (Trillions USD)",
            xlabel="Year")
    plt.legend(title="Country")

    return ax