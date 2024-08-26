# Complete code to generate the plot with the specified adjustments

import matplotlib.pyplot as plt
import numpy as np
# plt.rcParams['font.sans-serif']=['Times New Roman']
# plt.rcParams['axes.unicode_minus']=False
data_cifar10 = {
    # "Krum": [[82.3, 81.42, 78.86, 65.11],#ratio
    #                      [71.04, 69.67, 51.11, 50.86],
    #                      [68.74, 48.57, 48.44, 48.42],
    #                      [71.04, 69.67, 70.48, 70]],
                "MKrum": [[81.11, 81.67, 79.9, 73],
                          [80.3, 67.67, 52, 56.78],
                          [79.78, 68.33, 67.43, 65.89],
                          [82, 82.67, 82.38, 80.11]],
                "Median": [[81.7, 81.17, 77.24, 67.67],
                           [78.52, 77.08, 69.81, 59.22],
                           [78, 77.75, 66.86, 66.44],
                           [80.22, 76.17, 75.05, 45.89]],
                "RFA": [[82.3, 80.75, 78, 60.67],
                        [80.52, 78.08, 74.76, 48.44],
                        [81.04, 78.42, 73.71, 48.56],
                        [79.93, 78.17, 36.48, 7.89]],
                "Trim": [[81.78, 81.58, 80.19, 74.78],
                         [80.52, 77.75, 72.67, 64.67],
                         [80.96, 76.42, 72.29, 69.11],
                         [8.52, 9.58, 10.95, 12.78]],
                "Cluster": [[81.93, 82.5, 82.57, 79.11],
                            [80.96, 79.42, 78.95, 78.56],
                            [80.67, 79.58, 78.86, 78.89],
                            [80.37, 81.25, 42, 72.78]],
                "FLTrust": [[82.37, 79.08, 72.1, 72.78],
                            [81.63, 81.58, 81.05, 80.78],
                            [83.04, 81.83, 80.19, 78.78],
                            [80.52, 78.75, 81.14, 79.11]],
                "Ditto": [[81.7, 82.92, 82.1, 80.22],
                          [81.26, 80.17, 79.33, 77.33],
                          [81.26, 81.11, 79.33, 77.67],
                          [8.52, 9.58, 10.95, 12.78]],
                "FedCAP": [[85.04, 85.58, 84.95, 84.44],
                          [84.96, 85.25, 84.00, 84.00],
                          [84.89, 85.33, 84, 83.89],
                          [85.11, 85.17, 84.29, 83.78]]}

data_emnist = {
    # "Krum": [[84.86, 82.64, 2.87, 3.02],
    #                      [75.43, 73.09, 55.99, 54.13],
    #                      [75.29, 67.05, 61.88, 61.09],
    #                      [76.15, 75.56, 59.72, 1.44]],
                "MKrum": [[84.52, 83.67, 3.02, 2.87],
                          [83.58, 78.83, 71.08, 64.48],
                          [83.76, 78.72, 71.68, 66.49],
                          [81.31, 63.52, 2.06, 3.02]],
                "Median": [[83.97, 82.94, 2.87, 3.02],
                           [82.16, 76.18, 70.31, 65.51],
                           [82.32, 75.93, 71.06, 63.66],
                           [82.38, 76.64, 65.88, 3.02]],
                "RFA": [[84.62, 82.41, 2.87, 3.02],
                        [83.89, 80.63, 71.55, 66.04],
                        [83.84, 80.49, 71.8, 64.43],
                        [83.79, 79.42, 19.06, 3.02]],
                "Trim": [[84.6, 83.71, 2.87, 3.02],
                         [83.42, 78.31, 69.59, 68.9],
                         [83.61, 79.31, 72.02, 68.82],
                         [3.11, 2.75, 2.87, 3.02]],
                "Cluster": [[84.69, 83.94, 2.87, 3.02],
                            [83.86, 82.73, 81.28, 78.47],
                            [83.8, 82.87, 81.61, 79.39],
                            [84.67, 84.06, 83.72, 3.02]],
                "FLTrust": [[77.21, 80.05, 2.87, 3.02],
                            [83.81, 83.55, 83.03, 83.04],
                            [83.88, 83.55, 83.37, 83.32],
                            [84.62, 84.16, 84.13, 84.13]],
                "Ditto": [[84.91, 84.52, 2.87, 3.02],
                          [84.22, 82.46, 79.07, 74.97],
                          [84.27, 82.78, 79.99, 76.9],
                          [3.11, 2.75, 2.87, 3.02]],
                "FedCAP": [[86.17, 85.7, 85.16, 85.15],
                          [86.11, 85.24, 85.39, 84.73],
                          [86.25, 85.81, 85.58, 84.8],
                          [86.51, 85.79, 85.43, 85.17]]}
# Data (randomly generated for the example)
fractions = np.array([10, 20, 30, 40])
methods = ["M-Krum", "Median", "RFA", "Trim.", "ClusteredFL", "FLTrust", "Ditto", "FedCAP"]
methods_abb = ["MKrum", "Median", "RFA", "Trim", "Cluster", "FLTrust", "Ditto", "FedCAP"]
attacks = ["LIE", "Min-Max", "Min-Sum", "IPM"]
markers = ['s', 'o', 'X', '^']
# data_mnist = {attack: np.random.uniform(50, 80, size=fractions.shape) for attack in attacks}
# data_cifar10 = {attack: np.random.uniform(30, 60, size=fractions.shape) for attack in attacks}

# Function to plot data without a legend
def plot_method_no_legend(i, ax, method, data, fractions):
    # linestyles = ['-', '--', ':', '-.', (0, (3, 1, 1, 1)), (0, (3, 5, 1, 5)), (0, (5, 10))]
    linestyles = ['-', '--', ':', '-.']
    for attack_idx, (attack, linestyle) in enumerate(zip(attacks, linestyles)):
        ax.plot(fractions, data[method][attack_idx], linestyle=linestyle, linewidth=3, label=attack, marker=markers[attack_idx], markersize=10)
    chartBox = ax.get_position()
    if i >= 8:
        ax.set_position([chartBox.x0-0.02, chartBox.y0-0.02,
                        chartBox.width * 0.8,
                        chartBox.height * 0.6])
    
    else:
        ax.set_position([chartBox.x0-0.02, chartBox.y0-0.1,
                        chartBox.width * 0.8,
                        chartBox.height * 0.6])
    
    ax.set_xticks(fractions)
    ax.set_ylim(0, 100)
    ax.tick_params(labelsize=18)

    ax.set_title(methods[methods_abb.index(method)], size=16)


# Create figure and subplots
fig, axs = plt.subplots(2, 8, figsize=(20, 5.5), constrained_layout=True)

# Plot data on subplots
for i, (ax, method) in enumerate(zip(axs.flatten(), methods_abb * 2)):
    if i < 8:
        plot_method_no_legend(i, ax, method, data_cifar10, fractions)
    else:
        plot_method_no_legend(i, ax, method, data_emnist, fractions)

    if i % 7 != 0:
        ax.set_ylabel('')
    # if i == 0:
    #     # ax.yaxis.set_label_position('right')
    #     ax.set_ylabel('CIFAR-10', size=20)
    # elif i == 8:
    #     # ax.yaxis.set_label_position('right')
    #     ax.set_ylabel('EMNIST', size=20)

# Remove subplot x and y labels
# for ax in axs.flatten():
#     ax.label_outer()
# Set common titles (moved to the correct positions)
fig.text(0.48, 0, 'Fraction of Malicious Clients (%)', ha='center', fontsize=18)
fig.text(0.05, 0.4, 'Test Accuracy', va='center', fontsize=18, rotation='vertical')
fig.text(0.065, 0.2, 'CIFAR-10', va='center', fontsize=16, rotation='vertical')
fig.text(0.065, 0.55, 'EMNIST', va='center', fontsize=16, rotation='vertical')
# fig.subplots_adjust(hspace=0.1)
# Create a legend for the whole figure
# lines = [plt.Line2D([0], [0], color='black', linestyle=ls) for ls in linestyles]
# fig.legend(lines, labels, loc='upper center', ncol=len(attacks), bbox_to_anchor=(0.5, 1.02))
lines, labels = fig.axes[0].get_legend_handles_labels()
fig.legend(lines, labels, ncol=len(attacks), bbox_to_anchor=(0.65, 0.8), fontsize=16)
# fig.tight_layout()
#plt.show()
plt.savefig('Figure10.pdf', bbox_inches='tight', pad_inches=0.0)