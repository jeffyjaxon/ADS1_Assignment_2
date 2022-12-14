import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_data(file_name):
    """
    Function reads data according to the file name passed as argument

    Parameters
    ----------
    file_name : String
        Name of file to be read.

    Returns
    -------
    data_col_year : DataFrame
        Returns dataframe with year as column and country as index.
    data_col_country : DataFrame
        Returns dataframe with country as column and year as index.

    """
    data = pd.read_excel(file_name, header=None, skiprows=4, index_col=False)
    data = data.rename(columns=data.iloc[0]).drop(data.index[0])
    data.drop(['Country Code', 'Indicator Name',
              'Indicator Code'], axis=1, inplace=True)

    # Filter dataframe with specific countries
    data_filter = return_dataframes(data)
    # Set Country Name as index
    data_final = data_filter.set_index('Country Name')
    data_final.index.name = None
    # Replace NaN values with 0
    data_final = data_final.fillna(0)
    data_col_year = data_final
    data_col_country = data_final.transpose()

    return data_col_year, data_col_country


def return_dataframes(data):
    """
    Function filters the dataframe with the countries in the list

    Parameters
    ----------
    data : DataFrame
        DataFrame to be filtered.

    Returns
    -------
    df_year_col : DataFrame
        Returns dataframe filtered with specific countries.

    """

    df_year_col = data[data["Country Name"].isin(countries)]
    return df_year_col


def bar_graph(data_col, data_row, title=""):
    """
    Function plots a bar graph with the datframe and title.

    Parameters
    ----------
    data_col : DataFrame
        DataFrame with year as column.
    data_row : DataFrame
        DataFrame with country as column.
    title : String, optional
        Title of the graph. The default is "".

    Returns
    -------
    None.

    """
    df = pd.DataFrame({'1980': data_col[2000.0],
                       '2000': data_col[2010.0],
                       '2020': data_col[2020.0]}, index=data_col.index)
    plt.figure()
    df.plot.bar()
    plt.title(title)
    plt.xlabel("Countries")
    plt.ylabel("Percentage (Unemployment)")
    plt.show()


def line_plot(dataframe, title=""):
    """
    Function plots a line graph with the dataframe and title passed as
    arguments

    Parameters
    ----------
    dataframe : DataFrame
        Data.
    title : TYPE, optional
        DESCRIPTION. The default is "".

    Returns
    -------
    None.

    """
    df = pd.DataFrame({'China': dataframe["China"],
                       'India': dataframe["India"],
                       'Japan': dataframe["Japan"],
                       'United Kingdom': dataframe["United Kingdom"]},
                      index=dataframe.index)

    filter_df = df[df.index.isin(years)]
    plt.figure()
    filter_df.plot.line()
    plt.title(title)
    plt.xlabel("Years")
    plt.xticks(years, rotation=90)
    plt.ylabel("Percentage(Fossil Fuel Consumption)")
    plt.legend()
    plt.show()


def df_generate(country):
    """
    Function returns the dataframe for generating heatmap with the country name
    passed as argument

    Parameters
    ----------
    country : DataFrame
        DataFrame with country as column.

    Returns
    -------
    DataFrame
        DataFrame to generate Heatmap.

    """

    heatmap_df = pd.DataFrame({'Indicator': indicators,
                               '2000': [total_unemployment_coun[country][2000.0],
                                        unemployment_male_coun[country][2000.0],
                                        unemployment_female_coun[country][2000.0],
                                        fossil_coun[country][2000.0],
                                        pollution_coun[country][2000.0],
                                        population_growth_coun[country][2000.0]],
                               '2010': [total_unemployment_coun[country][2010.0],
                                        unemployment_male_coun[country][2010.0],
                                        unemployment_female_coun[country][2010.0],
                                        fossil_coun[country][2010.0],
                                        pollution_coun[country][2010.0],
                                        population_growth_coun[country][2010.0]],
                               '2020': [total_unemployment_coun[country][2020.0],
                                        unemployment_male_coun[country][2020.0],
                                        unemployment_female_coun[country][2020.0],
                                        fossil_coun[country][2020.0],
                                        pollution_coun[country][2020.0],
                                        population_growth_coun[country][2020.0]]}
                              )

    return heatmap_df.set_index('Indicator')


def heatmap_plot(dataframe, title=""):
    """
    Function to plot heatmap with the dataframe as title passed as argument.

    Parameters
    ----------
    dataframe : DataFrame
        DataFrame to plot heatmap.
    title : String, optional
        Function plots a correlation heatmap. The default is "".

    Returns
    -------
    None.

    """
    plt.figure()
    dataframe.index.name = None
    heat = dataframe.transpose()
    sns.heatmap(heat.corr(), cmap='Greens', annot=True)
    plt.title(title)
    plt.show()


def avg_calculator(dataframe):
    """
    Function calculates the mean for the columns in the dataframe.

    Parameters
    ----------
    dataframe : DataFrame
        The dataframe whose mean value needs to be calculated.

    Returns
    -------
    avg_df : DataFrame
        DataFrame with the mean value.

    """
    avg_df = pd.DataFrame(
        {'Countries': countries,
         'Mean': [[dataframe[countries[0]].mean()][0],
                  [dataframe[countries[1]].mean()][0],
                  [dataframe[countries[2]].mean()][0],
                  [dataframe[countries[3]].mean()][0],
                  [dataframe[countries[4]].mean()][0],
                  [dataframe[countries[5]].mean()][0],
                  [dataframe[countries[6]].mean()][0],
                  [dataframe[countries[7]].mean()][0],
                  [dataframe[countries[8]].mean()][0]]
         }
    )
    return avg_df


# List of countries to filter dataframe
countries = ["India", "Sudan", "China", "Germany", "United Kingdom",
             "Japan", "Somalia", "Bangladesh", "Saudi Arabia"]

# List of indicators used
indicators = ['Total Unemployment', 'Male Unemployment', 'Female Unemployment',
              'Fossil Fuel Consumption', 'PM2.5 Pollution',
              'Population Growth']

years = [2000.0, 2005.0, 2010.0, 2015.0, 2020.0]

# Read data from excel files for various files
total_unemployment_year, total_unemployment_coun = read_data(
    "Total_Unemployment.xls")
unemployment_male_year, unemployment_male_coun = read_data(
    "Unemployemnt_Male.xls")
unemployment_female_year, unemployment_female_coun = read_data(
    "Unemployment_Female.xls")
fossil_year, fossil_coun = read_data("Fossil_Fuel.xls")
pollution_year, pollution_coun = read_data("PM2.5_Pollution.xls")
population_growth_year, population_growth_coun = read_data(
    "Population_Growth.xls")

# Plotting Bar Graph for corresponding dataframes
bar_graph(total_unemployment_year, total_unemployment_coun,
          title="Percentage of Total Unemployemnt")

bar_graph(unemployment_male_year, unemployment_male_coun,
          title="Percentage of Unemployemnt - Male")

bar_graph(unemployment_female_year, unemployment_female_coun,
          title="Percentage of Unemployemnt - Female")

# Generate dataframe to plot Heatmaps
df_heatmap_china = df_generate("China")
df_heatmap_japan = df_generate("Japan")

# Plotting Heatmaps for different countries
heatmap_plot(df_heatmap_china, title="China")
heatmap_plot(df_heatmap_japan, title="Japan")

# Plotting Line Graph
line_plot(fossil_coun, title="Fossil Fuel Consumption")
line_plot(pollution_coun, title="PM2.5 Pollution Percentage")

# Prints the mean for the fossil fuel consumption
print(avg_calculator(fossil_coun))
