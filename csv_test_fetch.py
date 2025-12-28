import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

if __name__ == "__main__":
    df = pd.read_csv('Gen1_data.csv')
    print(df.head(151))
    print("Number of Rows: ", df.shape[0])
    print("Number of Columns: ", df.shape[1])
    print("Attributes/Column Names: ", df.columns)
    print("Missing data: ", df.isnull().sum()) 
    stat_columns = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
    print("Statistics of data: \n", df[stat_columns].describe())