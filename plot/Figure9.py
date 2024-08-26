import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# plt.rcParams['font.sans-serif']=['Times New Roman']
# plt.rcParams['axes.unicode_minus']=False
DATASET = ['CIFAR-10', 'EMNIST', 'WISDM']

INFO = DATASET

ATK = ['SF', 'MR', 'LIE', 'Min-Max', 'Min-Sum', 'IPM']
ACC = [[84.00, 84.10, 84.95, 84.00, 84.38, 84.29], # CIFAR10, EMNIST, WISDM
       [85.24, 85.82, 85.16, 85.39, 85.58, 85.43],
       [94.16, 95.07, 94.76, 94.06, 94.26, 94.06]]
DAcc = [[100, 100, 70, 100, 100, 100],
        [80, 100, 81, 93, 96, 98],
        [100, 100, 72.22, 100, 100, 100]]
Benign = [85.6, 86.59, 93.78]
FPR = [[0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]
FNR = [[0, 0, 100, 0, 0, 0],
       [20, 0, 63.33, 23.33, 13.33, 6.67],
       [0, 0, 100, 0, 0, 0]]

width = [0.15, 0.15, 0.15, 0.15]
ind = np.arange(len(ATK))

fig = plt.figure(figsize=(8.5, 4)) # 25, 14
gs00 = matplotlib.gridspec.GridSpec(3, 1)
# plt.rc('font', family='Times New Roman')
font_size = 18
plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False

for idx1, dataset in enumerate(DATASET):
    ax = fig.add_subplot(gs00[idx1])
    xlabels = ATK
    ax.bar(ind - width[idx1], ACC[idx1], width[idx1], color='#A6CEE3', label='TAcc', edgecolor='#000000')
    ax.bar(ind, DAcc[idx1], width[idx1], color='#A6CEE3', hatch='---', alpha=0.99, label='DAcc', edgecolor='#000000')#'#cd5c5c')
    # Benign_ACC = [Benign[idx1][idx2] - ACC[idx1][idx2] for idx2 in range(len(Benign[idx1]))]
    # ax.bar(ind - width[idx1] / 2, Benign_ACC[idx1], width[idx1], bottom=ACC[idx1], color='red', label='B-Acc', edgecolor='#000000')
    ax.bar(ind + width[idx1], FPR[idx1], width[idx1], color='#FB9A99', hatch='//', alpha=0.99, label='FPR', edgecolor='#000000')#'#cd5c5c')
    ax.bar(ind + width[idx1], FNR[idx1], width[idx1], hatch='\\\\', color='#B2DF8A', alpha=0.99, label='FNR', edgecolor='#000000')#'#8fbc8b')
    ax.set(ylim=(0, 100), yticks=np.arange(0, 101, 50), xticks=ind)
    # if idx1 == 0:
    #     ax.legend(ncol=4, fontsize=30)
    ax.set_xticklabels(xlabels)

    # if idx1 == 0:
    #     ax.set_title('{}'.format(ATK[idx2]), fontsize=32)
    # if idx2 == 0:
    #     ax.set_ylabel(INFO[idx1][0], fontsize=28, rotation=0, labelpad=42)
    ax.tick_params(labelsize=18)
    chartBox = ax.get_position()
    ax.set_position([chartBox.x0, chartBox.y0,
                    chartBox.width,
                    chartBox.height * 0.65])
    ax.set_ylabel(INFO[idx1], fontsize=16)
    ax.axhline(Benign[idx1], color='red')
    # ax.set_title(dataset, size=18)

# fig.text(0.53, 0, 'Clustering Identity', va='center', ha='center', fontsize=32)
lines, labels = fig.axes[0].get_legend_handles_labels()
fig.text(0.98, 0.5, 'Test Accuracy', va='center', fontsize=18, rotation='vertical')
fig.legend(lines, labels, ncol=4, bbox_to_anchor=(0.87, 1), fontsize=14)

# fig.tight_layout()
# plt.show()
# plt.legend()

# plt.show()
plt.savefig('Figure9.pdf', bbox_inches='tight', pad_inches=0.0)