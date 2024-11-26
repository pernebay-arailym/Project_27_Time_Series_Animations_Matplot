import pandas as pd 
import matplotlib.pyplot as plt

pop_data = pd.read_csv('/Users/pernebayarailym/Documents/Portfolio Projects AP/Python Projects/Project_27_Time_Series_Animations_Matplot/data/cleaned-data.csv')

pop_data_1950 = pop_data[pop_data['Time'] == 1950]

top_countries = pop_data_1950.nlargest(10, 'TPopulation1Jan')

plt.barh(top_countries['Location'], top_countries['TPopulation1Jan'])