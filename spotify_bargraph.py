import matplotlib.pyplot as plt
import numpy as np

high_tempo = 134.73
low_tempo = 123.33

plt.rcdefaults()
fig, ax = plt.subplots()

# create the graph
tempo = ('High Temp', 'Low Tempo')
y_pos = np.arange(len(tempo))
tempos = (high_tempo, low_tempo)


error = np.random.rand(len(tempo))

ax.barh(y_pos, tempos, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(tempo)
ax.invert_yaxis()
ax.set
ax.set_ylabel("Most Popular Songs")
ax.set_xlabel('Tempo')
ax.set_title('Average Tempos for Popular and Unpopular Christmas Songs on Spotify')
ax.barh(y_pos, tempos, color=('red', 'green'))

plt.show()