import os
import numpy as np

# folder_path = "../../try/FedCAP/results/npz/Table2"
# file_list = sorted(os.listdir(folder_path))
# print(file_list)
file_list = ['cifar10_pat_FedAvg_A5_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc20_seed0_RAMmedian.npz', 'cifar10_pat_FedAvg_A5_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc20_seed0_RAMmkrum.npz', 'cifar10_pat_FedAvg_A5_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc20_seed0_RAMrfa.npz', 'cifar10_pat_FedAvg_A8_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc20_seed0_RAMmedian.npz', 'cifar10_pat_FedAvg_A8_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc20_seed0_RAMmkrum.npz', 'cifar10_pat_FedAvg_A8_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc20_seed0_RAMrfa.npz', 'cifar10_pat_FedCAP_A5_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc20_seed0_lamda0.1_alpha10_phi0.2_normT10.npz', 'cifar10_pat_FedCAP_A8_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc20_seed0_lamda0.1_alpha10_phi0.3_normT10.npz', 'emnist_group_FedAvg_A5_0.3_bz10_lr0.01_gr100_ep5_jr0.2_nc100_seed0_RAMmedian.npz', 'emnist_group_FedAvg_A5_0.3_bz10_lr0.01_gr100_ep5_jr0.2_nc100_seed0_RAMmkrum.npz', 'emnist_group_FedAvg_A5_0.3_bz10_lr0.01_gr100_ep5_jr0.2_nc100_seed0_RAMrfa.npz', 'emnist_group_FedAvg_A8_0.3_bz10_lr0.01_gr100_ep5_jr0.2_nc100_seed0_RAMmedian.npz', 'emnist_group_FedAvg_A8_0.3_bz10_lr0.01_gr100_ep5_jr0.2_nc100_seed0_RAMmkrum.npz', 'emnist_group_FedAvg_A8_0.3_bz10_lr0.01_gr100_ep5_jr0.2_nc100_seed0_RAMrfa.npz', 'emnist_group_FedCAP_A5_0.3_bz10_lr0.01_gr100_ep5_jr0.2_nc100_seed0_lamda0.5_alpha10_phi0.1_normT10.npz', 'emnist_group_FedCAP_A8_0.3_bz10_lr0.01_gr100_ep5_jr0.2_nc100_seed0_lamda0.5_alpha10_phi0.1_normT10.npz', 'wisdm_nature_FedAvg_A5_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc36_seed0_RAMmedian.npz', 'wisdm_nature_FedAvg_A5_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc36_seed0_RAMmkrum.npz', 'wisdm_nature_FedAvg_A5_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc36_seed0_RAMrfa.npz', 'wisdm_nature_FedAvg_A8_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc36_seed0_RAMmedian.npz', 'wisdm_nature_FedAvg_A8_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc36_seed0_RAMmkrum.npz', 'wisdm_nature_FedAvg_A8_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc36_seed0_RAMrfa.npz', 'wisdm_nature_FedCAP_A5_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc36_seed0_lamda0.1_alpha1_phi0.2_normT10.npz', 'wisdm_nature_FedCAP_A8_0.3_bz10_lr0.01_gr100_ep5_jr1.0_nc36_seed0_lamda0.1_alpha2_phi0.1_normT10.npz']
for file_name in file_list:
    file_path = os.path.join('../results/npz', file_name)
    with np.load(file_path, allow_pickle=True) as f:
        test_acc_g = f['test_acc_g'][-1]*100
        test_acc_p = f['test_acc_p'][-1]*100
        # test_acc_g = np.random.uniform(low=0, high=1, size=101)[-1]*100
        # test_acc_p = np.random.uniform(low=0, high=1, size=101)[-1]*100
        max_test_acc = max(test_acc_g, test_acc_p)
        print('Table 2 \n{}: {:.2f}'.format(file_name, max_test_acc))