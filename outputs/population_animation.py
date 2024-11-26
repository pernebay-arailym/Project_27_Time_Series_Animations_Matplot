import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

pop_data = pd.read_csv('/Users/pernebayarailym/Documents/Portfolio Projects AP/Python Projects/Project_27_Time_Series_Animations_Matplot/data/cleaned-data.csv')

frames = pop_data['Time'].unique()

fig, ax = plt.subplots(figsize=(12,6))

#plt.barh(top_countries['Location'], top_countries['TPopulation1Jan'])

def animate(frame):
    ax.clear()

    pop_data_frame = pop_data[pop_data['Time'] == frame] 

    top_countries = pop_data_frame.nlargest(10, 'TPopulation1Jan').sort_values('TPopulation1Jan', ascending=True)
    ax.barh(top_countries['Location'], top_countries['TPopulation1Jan'])

anim = animation.FuncAnimation(fig, animate, frames=frames, interval=200)
plt.show()