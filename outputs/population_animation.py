import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def setup_plot_style(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='y', which='both', left=False)
    ax.tick_params(axis='x', which='both', bottom=False)
    ax.set_xlabel('Total population on 1st January')
    ax.set_title('Top 10 Countries by Population')


def create_animation(df):

    df = pd.read_csv('/Users/pernebayarailym/Documents/Portfolio Projects AP/Python Projects/Project_27_Time_Series_Animations_Matplot/data/cleaned-data.csv')

    frames = df['Time'].unique()

    fig, ax = plt.subplots(figsize=(12,6))

    #plt.barh(top_countries['Location'], top_countries['TPopulation1Jan'])

    def animate(frame):
        ax.clear()

        pop_data_frame = df[df['Time'] == frame] 

        top_countries = pop_data_frame.nlargest(10, 'TPopulation1Jan').sort_values('TPopulation1Jan', ascending=True)
        ax.barh(top_countries['Location'], top_countries['TPopulation1Jan'])

    anim = animation.FuncAnimation(fig, animate, frames=frames, interval=200)
    return anim

if __name__ == '__main__':
    df =pd.read_csv('/Users/pernebayarailym/Documents/Portfolio Projects AP/Python Projects/Project_27_Time_Series_Animations_Matplot/data/cleaned-data.csv')
    anim=create_animation(df)
    anim.save('video.mp4', writer='ffmpeg', fps=30)  
    plt.show()