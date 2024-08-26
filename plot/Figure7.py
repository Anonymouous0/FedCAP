import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
# plt.rcParams['font.sans-serif']=['Times New Roman']
# plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(20, 5))
width = 0.25
bar_loc = [-width*3, -width*2, -width, 0, width, width*2, width*3]
ind = np.arange(0, 3*2, 2)
color = ['#F2F2F2', '#D5D5D5', '#A1A1A1', '#4F4F4F', '#E2E8F0', '#FADBD8']
edgecolor = ['black', 'black', 'black', 'black', '#3282b8', '#810000']
hatch = [None, None, None, None, '\\\\\\', '---']
CIFAR_Info = {'FedAvg': [38.27, 36.19, 10.95, 3.43],
              'FedAvg-FT': [82.13, 80.48, 10.95, 10.19],
              #'FLTrust': [82.80, 82.67, 82.19, 20.67],
              'Ditto': [82.73, 80.67, 10.95, 69.05],
              'FedRoD': [82.33, 80.67, 10.95, 81.14],
              'FedFomo': [84.73, 81.81, 81.81, 84.10],
              'FedCAP': [85.60, 83.71, 84.00, 84.10]}

EMNIST_Info = {'FedAvg': [72.09, 69.33, 62.31, 5.18],
              'FedAvg-FT': [84.72, 83.76, 78.15, 12.56],
              #'FLTrust': [84.72, 83.92, 84.05, 3.01],
              'Ditto': [84.93, 83.71, 78.43, 63.39],
              'FedRoD': [80.99, 79.90, 74.14, 4.94],
              'FedFomo': [82.64, 81.48, 81.83, 81.52],
              'FedCAP': [86.59, 83.97, 85.24, 85.82]}


WISDM_Info = {'FedAvg': [86.47, 77.54, 37.36, 37.36],
              'FedAvg-FT': [93.05, 92.95, 37.36, 37.36],
              #'FLTrust': [93.27, 92.65, 93.35, 37.36],
              'Ditto': [93.78, 92.95, 89.10, 37.36],
              'FedRoD': [93.49, 92.85, 37.36, 37.36],
              'FedFomo': [89.17, 89.63, 89.73, 89.83],
              'FedCAP': [93.78, 93.45, 94.16, 95.07]}

for i, atk in enumerate(['Benign', 'LF', 'SF', 'MR']):

    if i == 0:
        width = 0.25
    else: 
        width = 0.25
        ind = np.arange(0, 3*2, 2)
    ax = plt.subplot(2, 2, i+1)
    if i == 0:
        ind = np.arange(0, 2.3*3, 2.3)
        x = ind - width * 4
        y = [78.8, 68.01, 89.98]
        axl = ax.bar(x, y, width, color='white', label='Local',
        hatch=None, edgecolor='black')
        ax.bar_label(axl, fmt='%.1f', fontsize=10, rotation=50)
        ax.set_xticks(ind)
    for j, method in enumerate(CIFAR_Info.keys()):
        
        x = ind + bar_loc[j]
        y = [CIFAR_Info[method][i], EMNIST_Info[method][i], WISDM_Info[method][i]]
        axl = ax.bar(x, y, width, color=color[j], label=method,
        hatch=hatch[j], edgecolor=edgecolor[j])
        ax.bar_label(axl, fmt='%.1f', fontsize=10, rotation=50)
        ax.set_xticks(ind)

    ax.set_ylim((0, 100))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
    ax.set_xticklabels(('CIFAR-10', 'EMNIST', 'WISDM'))
    chartBox = ax.get_position()
    ax.set_position([chartBox.x0, chartBox.y0,
                    chartBox.width*1.1,
                    chartBox.height * 0.85])
    
    if i == 0 or i == 2:
        ax.set_ylabel('Test Accuracy', fontsize=18)
    ax.set_title('{}'.format(atk), fontsize=18)
    ax.tick_params(labelsize=14)

lines, labels = fig.axes[0].get_legend_handles_labels()
fig.legend(lines, labels, ncol=8, bbox_to_anchor=(0.8, 1), fontsize=14)
# fig.tight_layout()
# plt.plot()
plt.savefig('Figure7.pdf', bbox_inches='tight', pad_inches=0.0)
