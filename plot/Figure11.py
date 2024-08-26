import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
# plt.rcParams['font.sans-serif']=['Times New Roman']
# plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(8, 2.5))

x = ['2', '5', '10']

data = {'CIFAR-10': [[82.27, 84.47, 85.60],
                    [82.86, 82.86, 84.89],
                    (82, 86)],
        'EMNIST': [[84.74, 84.86, 86.59],
                   [83.20, 84.29, 85.36],
                   (83, 87)],
        'WISDM': [[93.78, 93.78, 93.64, 92.68],
                  [93.76, 94.06, 93.76, 93.25],
                  (92, 95)]}

dataset = list(data.keys())

for i in range(len(dataset)):
    if dataset[i] == 'WISDM':
        x = [1, 2, 3, 4]
    ax1 = plt.subplot(1, 3, i+1)
    ax1.plot(x, data[dataset[i]][0], label='Benign', marker='s', linewidth=3, markersize=10)
    ax1.plot(x, data[dataset[i]][1], label='IPM', marker='^', linewidth=3, markersize=10)
    ax1.set_title('{}'.format(dataset[i]), fontsize=18)
# ax1.set_ylabel('Test Accuracy', fontsize=18)
    ax1.tick_params(labelsize=14)
    #ax1.set_xticks(x, rotation=0)
    ax1.set_xticks(x)
    ax1.set_xticklabels(x, rotation=0)
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(4))
    ax1.set(ylim=data[dataset[i]][2], yticks=np.arange(data[dataset[i]][2][0], data[dataset[i]][2][1]+1, 1), xticks=x)
    ax1.set_ylim()
    if i == 0:
        ax1.set_ylabel('Test Accuracy', fontsize=16)
    elif i == 1:
        chartBox = ax1.get_position()
        ax1.set_xlabel(r'$\alpha$', fontsize=16)
        ax1.set_position([chartBox.x0, chartBox.y0,
                    chartBox.width,
                    chartBox.height* 1.2])
lines, labels = fig.axes[0].get_legend_handles_labels()
fig.legend(lines, labels, ncol=4, bbox_to_anchor=(0.73, 1), fontsize=16)
fig.tight_layout()
# plt.show()
plt.savefig('Figure11.pdf', bbox_inches='tight', pad_inches=0.0)