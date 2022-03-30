# task6_15.py
"""
Intro to data science: Dynamic Visualization of rolling two dice.
Create two dice rolling simulation and update bar plot dynamically.
"""
import matplotlib.pyplot as plt
from matplotlib import animation
import random
import seaborn as sns

#update the bar plot
def update(frame_number, tosses, faces, frequencies, count): #frame_number - argument must be by default when FuncAniamtion() is used
    count[0] += 1
    for toss in range(tosses):
        frequencies[random.randrange(2,13) - 2] += 1

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
        axes.text(text_x, text_y, text, ha='center', va='bottom',fontsize=8)

#Defining update() parameters:
number_of_frames = 6_000
tosses_per_frame = 100   #=tosses
values = list(range(2,13))
frequencies = [0] * 11
count1 = [0]
# count1[0] = 0

#Defining FuncAnimatio() parameters:
sns.set_style('whitegrid')
figure = plt.figure('Two Dice Roll')  #figure to display animation

#Start animation and call update()
coin_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=10,
    fargs=(tosses_per_frame, values, frequencies, count1)
)

fig1 = plt.gcf() #gcf() - get current figure
plt.show() #show bar plot
fig1.savefig(f'2dice_roll{sum(frequencies):,}times.pdf', bbox_inches='tight') #save out figure, which contains animation

"""
output for zip() section --> unpack axes.patches:
1.100.bar: Rectangle(xy=(-0.4, 0), width=0.8, height=7, angle=0) frequency:7
1.100.bar: Rectangle(xy=(0.6, 0), width=0.8, height=8, angle=0) frequency:8
1.100.bar: Rectangle(xy=(1.6, 0), width=0.8, height=8, angle=0) frequency:8
1.100.bar: Rectangle(xy=(2.6, 0), width=0.8, height=7, angle=0) frequency:7
1.100.bar: Rectangle(xy=(3.6, 0), width=0.8, height=9, angle=0) frequency:9
1.100.bar: Rectangle(xy=(4.6, 0), width=0.8, height=7, angle=0) frequency:7
1.100.bar: Rectangle(xy=(5.6, 0), width=0.8, height=10, angle=0) frequency:10
1.100.bar: Rectangle(xy=(6.6, 0), width=0.8, height=17, angle=0) frequency:17
1.100.bar: Rectangle(xy=(7.6, 0), width=0.8, height=6, angle=0) frequency:6
1.100.bar: Rectangle(xy=(8.6, 0), width=0.8, height=10, angle=0) frequency:10
1.100.bar: Rectangle(xy=(9.6, 0), width=0.8, height=11, angle=0) frequency:11
2.200.bar: Rectangle(xy=(-0.4, 0), width=0.8, height=14, angle=0) frequency:14
2.200.bar: Rectangle(xy=(0.6, 0), width=0.8, height=19, angle=0) frequency:19
2.200.bar: Rectangle(xy=(1.6, 0), width=0.8, height=15, angle=0) frequency:15
2.200.bar: Rectangle(xy=(2.6, 0), width=0.8, height=12, angle=0) frequency:12
"""


























