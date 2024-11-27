import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def setup_plot_style(ax):
    # Show only x and y-axis lines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#333333')
    ax.spines['bottom'].set_color('#333333')
    ax.tick_params(axis='y', which='both', left=False)
    ax.tick_params(axis='x', which='both', bottom=False, colors='#333333')
    ax.set_facecolor('white')  # Standard white background
    ax.set_xlabel('Total population', fontsize=14, labelpad=10, color='#333333')
    ax.set_title('Top 10 Countries by Population (in millions)', fontsize=18, pad=20, color='#333333')

def add_year_text(ax, year):
    # Place the year at the bottom-right corner
    ax.text(0.95, 0.05, str(year), transform=ax.transAxes, fontsize=24, ha='center', va='center', 
            bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.5'))

def create_animation(df):

    df = pd.read_csv('/Users/pernebayarailym/Documents/Portfolio Projects AP/Python Projects/Project_27_Time_Series_Animations_Matplot/data/cleaned-data.csv')

    frames = df['Time'].unique()

    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor('white')  # Set entire figure background to white

    def animate(frame):
        ax.clear()
        pop_data_frame = df[df['Time'] == frame]
        top_countries = pop_data_frame.nlargest(10, 'TPopulation1Jan').sort_values('TPopulation1Jan', ascending=True)
        colors = plt.cm.tab10.colors  # Vibrant color palette

        bars = ax.barh(top_countries['Location'], top_countries['TPopulation1Jan'], color=colors, edgecolor='black', height=0.7)

        # Add rounded edges to bars
        for bar in bars:
            bar.set_linewidth(0.5)
            bar.set_capstyle('round')

        # Add labels inside bars
        for i, row in top_countries.iterrows():
            ax.text(row['TPopulation1Jan'] - row['TPopulation1Jan'] * 0.02, row['Location'], 
                    f"{row['TPopulation1Jan']:,.2f}", va='center', ha='right', color='white', fontsize=10, weight='bold')

        setup_plot_style(ax)
        add_year_text(ax, frame)
        
        # Adding the graph title at both the top and bottom
        ax.set_title('Top 10 Countries by Population (in millions)', fontsize=18, pad=20, color='#333333')
        #plt.suptitle('Top 10 Countries by Population (in millions)', fontsize=18, color='#333333', y=0.95)

        plt.tight_layout()

    anim = animation.FuncAnimation(fig, animate, frames=frames, interval=1000)  # Set interval to 1000ms (1 second)
    
    return anim

if __name__ == '__main__':
    df = pd.read_csv('/Users/pernebayarailym/Documents/Portfolio Projects AP/Python Projects/Project_27_Time_Series_Animations_Matplot/data/cleaned-data.csv')
    anim = create_animation(df)
    anim.save('video.mp4', writer='ffmpeg', fps=30)
    plt.show()
