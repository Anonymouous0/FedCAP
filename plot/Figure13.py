import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

fig = plt.figure(figsize=(8, 2.5))
# plt.rcParams['font.sans-serif']=['Times New Roman']
# plt.rcParams['axes.unicode_minus']=False
x = ['0.1', '0.5', '1']

data = {'CIFAR-10': [[85.53, 85.13, 84.93],
                    [84.1, 83.9, 84.29],
                    (83, 86)],
        'EMNIST': [[85.10, 85.34, 85.14],
                   [83.96, 84.36, 83.9],
                   (83, 86)],
        'WISDM': [[93.78, 93.2, 93.27],
                  [94.06, 93.55, 93.35],
                  (93, 95)]}

dataset = list(data.keys())

for i in range(len(dataset)):
    ax1 = plt.subplot(1, 3, i+1)
    ax1.plot(x, data[dataset[i]][0], label='Benign', marker='s', linewidth=3, markersize=10)
    ax1.plot(x, data[dataset[i]][1], label='IPM', marker='^', linewidth=3, markersize=10)
    ax1.set_title('{}'.format(dataset[i]), fontsize=18)
# ax1.set_ylabel('Test Accuracy', fontsize=18)
    ax1.tick_params(labelsize=14)
    # ax1.set_xticks(x, rotation=0)
    ax1.set_xticks(x)
    ax1.set_xticklabels(x, rotation=0)
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(4))
    ax1.set(ylim=data[dataset[i]][2], yticks=np.arange(data[dataset[i]][2][0], data[dataset[i]][2][1]+1, 1), xticks=x)
    ax1.set_ylim()
    if i == 0:
        ax1.set_ylabel('Test Accuracy', fontsize=16)
    elif i == 1:
        chartBox = ax1.get_position()
        ax1.set_xlabel(r'$\lambda$', fontsize=16)
        ax1.set_position([chartBox.x0, chartBox.y0,
                    chartBox.width,
                    chartBox.height* 1.2])
lines, labels = fig.axes[0].get_legend_handles_labels()
fig.legend(lines, labels, ncol=4, bbox_to_anchor=(0.73, 1), fontsize=16)
fig.tight_layout()
# plt.show()
plt.savefig('Figure13.pdf', bbox_inches='tight', pad_inches=0.0)
