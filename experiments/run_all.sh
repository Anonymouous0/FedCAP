fig_num=(7 8 9 10 11 12 13)
tab_num=(1 2 3)

for fig in "${fig_num[@]}"; do
    chmod 775 experiments/Figure$fig.sh
    experiments/Figure$fig.sh > Figure$fig.log
done

for tab in "${tab_num[@]}"; do
    chmod 775 experiments/Table$tab.sh
    experiments/Table$tab.sh > Table$tab.log
done