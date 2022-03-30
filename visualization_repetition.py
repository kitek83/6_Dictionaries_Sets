#visualization_repetition
"""
Repetition of static visualization from previous chapter.
This script is without description.
Visualization for rolling die 60_000 times.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import random
import numpy as np

rolls = [random.randrange(1,7) for i in range(60_000)]
values, frequencies = np.unique(rolls, return_counts=True)

title = f'Rolling 6-sided-die {len(rolls):,} times.'    #:, - thousands seperator (format specifier)
sns.set_style('whitegrid')
axes = sns.barplot(x=values,y=frequencies, palette='bright')

axes.set_title(title)
axes.set_xlabel('Die Values')
axes.set_ylabel('Frequencies')

axes.set_ylim(top=max(frequencies) * 1.10)

for bar,frequency in zip(axes.patches ,frequencies):
    text_x = bar.get_x() + bar.get_width()/2
    text_y = bar.get_height()
    text = f'{frequency:,}\n {frequency/len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=12, ha='center', va='bottom')


print(f'{list(axes.patches)}')

plt.savefig(f'rolling_die_{len(rolls):,}times')
plt.show()






























