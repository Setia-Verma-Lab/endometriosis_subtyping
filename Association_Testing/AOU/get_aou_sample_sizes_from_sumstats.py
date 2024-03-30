import pandas as pd
import os

phenos = ['endometriosis']
phenos.extend([f'cluster_vs_controls_{i}' for i in range(1, 6)])

ancestries = ['AFR', 'EUR']

cases = pd.DataFrame(index=ancestries, columns=phenos)
controls = pd.DataFrame(index=ancestries, columns=phenos)
n_vars = pd.DataFrame(index=ancestries, columns=phenos)

for anc in ancestries:
    for pheno in phenos:
        df = pd.read_table(f'{anc}/Sumstats/{pheno}.saige.gz')
        cases.loc[anc, pheno] = df['N_case'].max()
        controls.loc[anc, pheno] = df['N_ctrl'].max()
        n_vars.loc[anc, pheno] = len(df)

cases.to_csv('AOU_case_counts.csv')
controls.to_csv('AOU_control_counts.csv')
n_vars.to_csv('AOU_variant_counts.csv')
