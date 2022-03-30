# dynamic_visualization.py
"""
This  script enhances the previous with the Matplotlib animation module's FuncAnimation()
function, which updates the bar plot dynamically.
"""
import sys # I will not use command line argument
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn as sns
import random

"""
frame_number - FuncAnimation requires the below 
update() to have this parameter, which is not used in the function
"""

def update(frame_number, rolls, faces, frequencies):
    """Configures barplot's contents for each animation frame"""
    #roll die and update frequencies
    for i in range(rolls):
        frequencies[random.randrange(1,7) - 1] += 1 #substract 1 to get corresponding index if frequencies, which increments due to die roll
    
    #configure the plot for updated die frequencies
    plt.cla()  #clear old contents, contents of current figure object

    axes = sns.barplot(x=faces, y=frequencies, palette='bright')  #creates bar plot

    axes.set_title(f'Die frequencies for {sum(frequencies):,} Rolls') #sum(frequencies), because we determine rolls_per_frame = 2 for 600 frames gives 1200 rolls
    axes.set_xlabel('Die Value')                                      #so this is not = rolls arguement
    axes.set_ylabel('Frequency')
    axes.set_ylim(top=max(frequencies) * 1.10)  #creates the free space for the text above each bar

    #display frequency and percentage above each patch bar
    for bar,frequency in zip(axes.patches, frequencies):  #zip()-enables iterate through multiple iterables / unpack tuple
        text_x = bar.get_x() + bar.get_width()/2
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency/sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')


#Defining func update()'s parameters
number_of_frames = 60_000
rolls_per_frame = 100             #rolls for update()
values = list(range(1,7))       #faces for update()
frequencies = [0] * 6           #frequencies for update()

sns.set_style('whitegrid')  #style for bar plot
figure = plt.figure('Rolling a six-sided-die.') #figure object in which FuncAnimations() displays an animation - this is popup window

#configure and start animation that calls function update()
die_animation = animation.FuncAnimation(
    figure,update, repeat=False, frames=number_of_frames, interval=2, #repeat=Fals - animation stops when reaches number_of_frames
    fargs=(rolls_per_frame, values, frequencies))   #fargs(function arguments) - arguments passed to update()

fig1 = plt.gcf() #gcf()-get currebnt figure - save current figure before you show, then you can call savefig() on this figure not to get empty graph
plt.show() #seaborn lib works together with matplotlip lib; plt() belongs to matplotlib.pyplot module
fig1.savefig(f'roll_die{sum(frequencies)}times.pdf',bbox_inches='tight') #2nd arg trims extra whitespace from the plot





















