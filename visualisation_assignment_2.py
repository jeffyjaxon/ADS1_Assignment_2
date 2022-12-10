import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_data(data_name):
    """
    This function reads the excel file and returns two dataframes.
    data_col_year = Returns dataframe with year as columns
    data_col_country = Returns dataframe with country as columns

    """
    data = pd.read_excel(data_name, header=None, skiprows=4, index_col=False)
    data = data.rename(columns=data.iloc[0]).drop(data.index[0])
    data.drop(['Country Code', 'Indicator Name',
              'Indicator Code'], axis=1, inplace=True)

    data_filter = return_dataframes(data)
    data_final = data_filter.set_index('Country Name')
    data_final.index.name = None
    data_final = data_final.fillna(0)
    data_col_year = data_final

    data_col_country = data_final.transpose()

    # data_col_year.index.name = "Country Name"
    # data_col_country.index.name = "Year"

    return data_col_year, data_col_country


def return_dataframes(data):

    df_year_col = data[data["Country Name"].isin(countries)]
    return df_year_col


def bar_graph(data_col, data_row, title=""):
    df = pd.DataFrame({'1980': data_col[2000.0],
                       '2000': data_col[2010.0],
                       '2020': data_col[2020.0]}, index=data_col.index)
    df.plot.bar()
    plt.title(title)

def heat_plot(dataframe, size=6):
    corr = dataframe.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr, cmap='coolwarm')
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)

def line_plot(dataframe, title=""):
    df = pd.DataFrame({'China': dataframe["China"],
                       'India': dataframe["India"],
                       'Japan': dataframe["Japan"],
                       'United Kingdom': dataframe["United Kingdom"]}, index=dataframe.index)
    df.plot.line()
    plt.title(title)

countries = ["India", "Sudan", "China", "Germany", "United Kingdom",
             "Japan", "Somalia", "Bangladesh", "Saudi Arabia"]

# def pie_plot():
        

total_unemployment_year, total_unemployment_coun = read_data("Total_Unemployment.xls")
unemployment_male_year, unemployment_male_coun = read_data("Unemployemnt_Male.xls")
unemployment_female_year, unemployment_female_coun = read_data("Unemployment_Female.xls")
fossil_year, fossil_coun = read_data("Fossil_Fuel.xls")
pollution_year, pollution_coun = read_data("PM2.5_Pollution.xls")
population_growth_year, population_growth_coun = read_data("Population_Growth.xls")

bar_graph(total_unemployment_year, total_unemployment_coun, title="Total Unemployemnt")
bar_graph(unemployment_male_year, unemployment_male_coun, title="Unemployemnt Male")
bar_graph(unemployment_female_year, unemployment_female_coun, title="Unemployemnt Female")

indicators = ['Total Unemployment', 'Male Unemployment', 'Female Unemployment',
              'Fossil Fuel Consumption', 'PM2.5 Pollution', 'Population Growth',]

heatmap_df = pd.DataFrame({'Indicator': indicators, 
                           '2000': [total_unemployment_coun["China"][2000.0], 
                                    unemployment_male_coun["China"][2000.0],
                                    unemployment_female_coun["China"][2000.0],
                                    fossil_coun["China"][2000.0],
                                    pollution_coun["China"][2000.0],
                                    population_growth_coun["China"][2000.0]],
                           '2010':[total_unemployment_coun["China"][2010.0], 
                                    unemployment_male_coun["China"][2010.0],
                                    unemployment_female_coun["China"][2010.0],
                                    fossil_coun["China"][2010.0],
                                    pollution_coun["China"][2010.0],
                                    population_growth_coun["China"][2010.0]],
                           '2020':[total_unemployment_coun["China"][2020.0], 
                                    unemployment_male_coun["China"][2020.0],
                                    unemployment_female_coun["China"][2020.0],
                                    fossil_coun["China"][2020.0],
                                    pollution_coun["China"][2020.0],
                                    population_growth_coun["China"][2020.0]]}
         )
df_heatmap = heatmap_df.set_index('Indicator')

plt.figure()
df_heatmap.index.name = None
heat = df_heatmap.transpose()
sns.heatmap(heat.corr(), cmap='PuOr')
plt.show()


line_plot(fossil_coun, title ="Fossil Fuel Consumption")
line_plot(pollution_coun, title ="PM2.5 Pollution")
