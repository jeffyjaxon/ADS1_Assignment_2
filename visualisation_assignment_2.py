import pandas as pd

def read_data(data_name):
    """
    This function reads the excel file and returns two dataframes.
    data_col_year = Returns dataframe with year as columns
    data_col_country = Returns dataframe with country as columns

    """
    data = pd.read_excel(data_name, header=None, skiprows=4, index_col=False)
    data = data.rename(columns=data.iloc[0]).drop(data.index[0])
    data.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1, inplace=True)
    data_final = data.set_index('Country Name')
    data_final.index.name = None
    
    data_col_year = data_final
    data_col_country = data_final.transpose()
    return data_col_year,data_col_country

agricultutal_land_year, agricultutal_land_coun = read_data("Agricultural_Land.xls")
print(agricultutal_land_year)
