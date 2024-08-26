import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
# plt.rcParams['font.sans-serif']=['Times New Roman']
# plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(8, 2.5))

x = ['0.1', '0.2', '0.3']

data = {'CIFAR-10': [[85.40, 85.53, 85.60],
                    [84.29, 83.71, 83.43],
                    (83, 86)],
        'EMNIST': [[86.59, 86.52, 86.48],
                   [85.43, 85.36, 85.19],
                   (85, 87)],
        'WISDM': [[93.78, 93.64, 93.42],
                  [94.06, 93.76, 93.45],
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
        ax1.set_xlabel(r'$\phi$', fontsize=16)
        ax1.set_position([chartBox.x0, chartBox.y0,
                    chartBox.width,
                    chartBox.height* 1.2])
lines, labels = fig.axes[0].get_legend_handles_labels()
fig.legend(lines, labels, ncol=4, bbox_to_anchor=(0.73, 1), fontsize=16)
fig.tight_layout()
# plt.show()
plt.savefig('Figure12.pdf', bbox_inches='tight', pad_inches=0.0)