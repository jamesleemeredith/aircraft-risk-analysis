"""
This module is for your final visualization code.
After you have done your EDA and wish to create some visualizations for you final jupyter notebook
A framework for each type of visualization is provided.
"""
# visualization packages
import matplotlib.pyplot as plt
from matplotlib.axes._axes import _log as matplotlib_axes_logger
from matplotlib.ticker import FuncFormatter
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
plt.style.use('seaborn-whitegrid')
sns.set_style("white")
sns.set_context("poster")


def sample_plot_1():
    """
    This is a sample visualization function to show what one looks like.
    The code is borrowed from https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/

    This function takes no arguments and shows a nice visualization without having all your code in the notebook itself.
    """
    # Import dataset 
    df = dp.full_clean("data/Aviation_Data.csv","data/Aviation_Data_Cleaned.csv")
    
    # Create Filters
    top_makes_list = df['make'].value_counts().nlargest(10).index.tolist()
    top_makes_filter = df['make'].isin(top_makes_list)
    
    top_models_list = df['model'].value_counts().nlargest(20).index.tolist()
    top_models_filter = df['model'].isin(top_models_list)

    # Prepare Data 
    data = df[top_makes_filter & top_models_filter].groupby(['make','model'])['event_id'].count().reset_index()
    pivot_table_make_model = pd.pivot_table(df[top_makes_filter & top_models_filter], 
                                        values='passenger_count', 
                                        index='model', 
                                        columns='make', 
                                        aggfunc='count')
    pivot_data = pivot_table_make_model.sort_values(by=list(pivot_table_make_model.columns), ascending=False)

    # create ax element
    fig, ax = plt.subplots(figsize=(11, 11))
    # Draw the heatmap with the rocket color pallete and correct color map
    cmap = sns.color_palette("rocket_r", as_cmap=True)
    hue = data['event_id'].tolist().sort()
    sns.heatmap(pivot_data, 
                cmap=cmap, 
                robust=True,
                annot=True,
                fmt=",g",
                ax=ax
               )

    ax.set_title('Common Makes & Models to Avoid');
    
    pass

def sample_plot2():
    """
    This is a sample visualization function to show what one looks like.
    The code is borrowed from https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/

    This function takes no arguments and shows a nice visualization without having all your code in the notebook itself.
    """

    plt.figure(figsize=(16, 10), dpi=80)
    # Import Data
    df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

    # Draw Plot
    plt.figure(figsize=(16,10), dpi= 80)
    sns.kdeplot(df.loc[df['cyl'] == 4, "cty"], shade=True, color="g", label="Cyl=4", alpha=.7)
    sns.kdeplot(df.loc[df['cyl'] == 5, "cty"], shade=True, color="deeppink", label="Cyl=5", alpha=.7)
    sns.kdeplot(df.loc[df['cyl'] == 6, "cty"], shade=True, color="dodgerblue", label="Cyl=6", alpha=.7)
    sns.kdeplot(df.loc[df['cyl'] == 8, "cty"], shade=True, color="orange", label="Cyl=8", alpha=.7)

    # Decoration
    plt.title('Density Plot of City Mileage by n_Cylinders', fontsize=22)
    plt.gca().set(xlabel='Mileage per Gallon in the City', ylabel='Kernel Denisty')
    plt.legend()
    plt.savefig('./images/viz2.png', transparent = True)
    plt.show()

    pass


def visualization_one(target_var = None, input_vars= None, output_image_name=None):
    """
    The visualization functions are what is used to create each individual image.
    The function should be repeatable if not generalizable
    The function will call either the boxplot or density plot functions you wrote above

    :param target_var:
    :param input_vars:
    :param output_image_name: the desired name for the image saved
    :return: outputs a saved png file and returns a fig object for testing
    """
    ###
    # Main chunk of code here
    ###

    # Starter code for labeling the image
    plt.xlabel(None, figure = fig)
    plt.ylabel(None, figure = fig)
    plt.title(None, figure= fig)
    plt.legend()

    # exporting the image to the img folder
    plt.savefig(f'images/{output_image_name}.png', transparent = True, figure = fig)
    return fig