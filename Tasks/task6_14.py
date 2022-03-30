# task6_14.py
"""
Intro to data science: Dynamic Visualization of coin tossing.
Create coin tossing simulation and update bar plot dynamically.
"""
import matplotlib.pyplot as plt
from matplotlib import animation
import random
import seaborn as sns

#update the bar plot
def update(frame_number, tosses, faces, frequencies, count): #frame_number - argument must be by default when FuncAniamtion() is used
    count[0] += 1
    for toss in range(tosses):
        frequencies[random.randrange(1,3) - 1]  += 1

    #Congigure the plot for updated frequencies
    plt.cla() #clear old animation figure to show new amimation frame's frequencies
    axes = sns.barplot(x=faces, y=frequencies, palette='bright')
    axes.set_title(f'Toss The Coin {sum(frequencies):,} times.')
    axes.set_xlabel('Coin Values')
    axes.set_ylabel('Frequencies')
    axes.set_ylim(top=max(frequencies) * 1.10) #additional space for the text above the plot's bar

    #display a frequency and procentage above aech patch bar
    #axex.patches - contains shapes and colors of plot's bars


    for bar, frequency in zip(axes.patches, frequencies): #unpack tuple(shape, frequncy)

        #to check:
        print(f'{count[0]}.{sum(frequencies)}.bar: {bar} frequency:{frequency}')
        text_x = bar.get_x() + bar.get_width()/2
        text_y = bar.get_height()   #bar.get_height()
        text = f'{frequency:,}\n{frequency/sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')

#Defining update() parameters:
number_of_frames = 6_000
tosses_per_frame = 100   #=tosses
values = ['heads','tails']  #for coin toss
frequencies = [0] * 2
count1 = [0]
# count1[0] = 0

#Defining FuncAnimatio() parameters:
sns.set_style('whitegrid')
figure = plt.figure('Toss Coin')  #figure to display animation

#Start animation and call update()
coin_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=10,
    fargs=(tosses_per_frame, values, frequencies, count1)
)

fig1 = plt.gcf() #gcf() - get current figure
plt.show() #show bar plot
fig1.savefig(f'toss_coin{sum(frequencies):,}times.pdf', bbox_inches='tight') #save out figure, which contains animation




























