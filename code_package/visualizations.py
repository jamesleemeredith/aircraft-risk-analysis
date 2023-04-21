"""
This module is for your final visualization code.
After you have done your EDA and wish to create some visualizations for you final jupyter notebook
A framework for each type of visualization is provided.
"""
# visualization packages
import matplotlib.pyplot as plt
from matplotlib.axes._axes import _log as matplotlib_axes_logger
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as mtick
import seaborn as sns
import code_package.data_preparation as dp

# Standard data manipulation packages
import pandas as pd
import numpy as np

matplotlib_axes_logger.setLevel('ERROR')

# Set specific parameters for the visualizations
large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
sns.set_style("dark")
sns.set_context("poster")
sns.color_palette("colorblind")


def commercial_fatality_rates(df):
    fig, ax = plt.subplots()
    data = df[df['top_make'] & (df['use_category'] == 'Commercial')]
    sns.barplot(data=data, 
                x='make', 
                y='fatality_rate',
                ax=ax,
               )
    ax.set_title('Fatality Rates by Make (Commercial)')
    ax.set_ylabel('Fatality Rate')
    ax.set_xlabel('Make')
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0, decimals=None))
    fig.savefig("images/commercial_fatality_rates_by_make.png");
    
    pass

def private_fatality_rates(df):
    fig, ax = plt.subplots()
    data = df[df['top_make']  & (df['use_category'] == 'Private')]
    sns.barplot(data=data, 
                x='make', 
                y='fatality_rate',
                ax=ax,
               )
    ax.set_title('Fatality Rates by Make (Private)')
    ax.set_ylabel('Fatality Rate')
    ax.set_xlabel('Make')
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0, decimals=None))
    fig.savefig("images/private_fatality_rates_by_make.png");

    pass

def private_models_fatality_rates(df):
    fig, ax = plt.subplots()
    df_filter = df['top_model'] & (df['use_category'] == 'Private')
    sns.barplot(data=df[df_filter], 
                x='fatality_rate',
                y='model',
                ax=ax,
               )
    ax.set_title('Fatality Rates by Model (Private)')
    ax.set_xlabel('Fatality Rate')
    ax.set_ylabel('Model')
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0, decimals=None))
    fig.savefig("images/private_fatality_rates_by_model.png");

    pass