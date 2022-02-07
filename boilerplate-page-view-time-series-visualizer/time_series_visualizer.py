import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
print(df)
# Clean data
df = df.drop(df[(df['value']<df['value'].quantile(0.025)) | (df['value']>df['value'].quantile(0.975))].index)
print(df)


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (15,5))
    ax.plot(df.index, df['value'], color='red',linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    print(df.index)
    df_bar['Month'] = pd.DatetimeIndex(df_bar.index).month
    df_bar['Year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot(kind='bar', legend = True, figsize = (15,10)).figure
    plt.xlabel('Years', fontsize=10)
    plt.ylabel('Average Page Views', fontsize=10)
    plt.xticks(fontsize = 10)
    plt.yticks(fontsize = 10)
    plt.legend(fontsize = 10, title="Months", labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Augues', 'September', 'October', 'November', 'December'])






    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = pd.DatetimeIndex(df_box['date']).year
    df_box['Month'] = pd.DatetimeIndex(df_box['date']).month

    # Draw box plots (using Seaborn)
    fig, (plt1, plt2) = plt.subplots(1, 2)
    fig.set_figwidth(20)
    fig.set_figheight(10)

    plt1 = sns.boxplot(x = df_box["Year"], y = df_box["value"], ax= plt1)
    plt1.set_title("Year-wise Box Plot (Trend)")
    plt1.set_xlabel('Year')
    plt1.set_ylabel('Page Views')

    plt2 = sns.boxplot(x = df_box["Month"], y = df_box["value"], ax=plt2)
    plt2.set_title("Month-wise Box Plot (Trend)")
    plt2.set_xlabel('Month')
    plt2.set_ylabel('Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig