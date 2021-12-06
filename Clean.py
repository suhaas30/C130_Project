import pandas as pd
import csv

df = pd.read_csv('final_dataset.csv')

df.columns

del df['Star_name_1']
del df['Luminosity']
del df['Distance_1']
del df['Mass_1']
del df['Radius_1']

final_data = df.dropna()

final_data.to_csv('main.csv')
 

