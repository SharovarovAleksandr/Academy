import matplotlib.pyplot as plt

fig = plt.figure()

ax_1 = fig.add_subplot(1, 4, 1)
ax_2 = fig.add_subplot(1, 4, 2)
ax_3 = fig.add_subplot(1, 4, 3)
ax_4 = fig.add_subplot(1, 4, 4)

ax_1.set(title = 'ax_1', xticks=[], yticks=[])
ax_2.set(title = 'ax_2', xticks=[], yticks=[])
ax_3.set(title = 'ax_3', xticks=[], yticks=[])
ax_4.set(title = 'ax_4', xticks=[], yticks=[])

plt.show()