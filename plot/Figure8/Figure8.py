import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
fig = plt.figure(figsize=(10, 4))

linestyles = ['--', '-.', 'dotted', (5, (10, 3)), '-']
atks = ["LIE", "Min-Max", "Min-Sum", "IPM"]
methods = ['Ditto', "Ditto+ClusteredFL", 'Ditto+Median', 'Ditto+Trim.', "FedCAP"]
DATASETS = ['CIFAR-10', "EMNIST"]
colors = ["#CF4B3E", "#F19839", "#4689BD", "#59AA4B", "#A080C4"]
import pandas as pd

count = 1
for d_idx, dataset in enumerate(DATASETS):
    for i, atk in enumerate(atks):
        ax1 = plt.subplot(2, 4, count)
        count+=1
        csv = pd.read_csv('Figure8/Ditto_AGR_{}.csv'.format(dataset))
        for j, alg in enumerate(methods):
            y = np.array(csv.iloc[:, 5*i+(j+1)])*100
            # print(y[-1])
            x = y.shape[0]
            ax1.plot(np.arange(x), y, label='{}'.format(alg), linestyle=linestyles[j], linewidth=2, color=colors[j])
        if d_idx == 0:
            ax1.set_title('{}'.format(atks[i]), fontsize=16)
        if i == 0:
            ax1.set_ylabel('{}'.format(DATASETS[d_idx]), fontsize=16, rotation='vertical')
        ax1.tick_params(labelsize=14)
        ax1.xaxis.set_major_locator(ticker.MultipleLocator(50))
        if count < 5:
            ax1.set_yticks((50, 81, 10))
            ax1.set_ylim(50, 90)
        else:
            ax1.set_yticks((0, 81, 20))
        ax1.yaxis.set_major_locator(ticker.MultipleLocator(20))
        chartBox = ax1.get_position()
        if d_idx == 0:
            ax1.set_position([chartBox.x0, chartBox.y0-0.07,
                            chartBox.width *0.95 ,
                            chartBox.height * 0.75])
            lines, labels = fig.axes[0].get_legend_handles_labels()
        else:
            ax1.set_position([chartBox.x0, chartBox.y0+0.01,
                            chartBox.width *0.95 ,
                            chartBox.height * 0.75])
            lines, labels = fig.axes[0].get_legend_handles_labels()

fig.legend(lines, labels, ncol=3, bbox_to_anchor=(0.88, 1), fontsize=16)
fig.text(0.03, 0.45, 'Test Accuracy', va='center', fontsize=16, rotation='vertical')
fig.text(0.5, 0.0, 'Global Rounds', ha='center', fontsize=16)
# fig.text(0.0, 0.5, 'Test Accuracy', va='center', rotation='vertical', fontsize=16)
# fig.tight_layout()
#plt.plot()
plt.savefig('Figure8.pdf', bbox_inches='tight', pad_inches=0.0)
