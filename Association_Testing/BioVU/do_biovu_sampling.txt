import pandas as pd
import numpy as np


def do_sampling(cluster_counts, output_pheno):
    cluster_groups = {}
    all_cases = output_pheno.index[output_pheno['endometriosis'] == 1]
    all_controls = output_pheno.index[output_pheno['endometriosis'] == 0]
    used_cases = []

    np.random.seed(314159)
    for pheno, count in cluster_counts.items():
        sample_cases = [c for c in all_cases if c not in used_cases]
        random_cases = np.random.choice(sample_cases, size=count, replace=False)
        used_cases.extend(random_cases)
        cluster_groups[pheno] = random_cases

    cluster_phenos = list(range(1, 6))

    output_pheno.loc[all_cases, cluster_phenos] = np.nan
    for pheno, case_list in cluster_groups.items():
        output_pheno.loc[case_list, pheno] = 1
        output_pheno.loc[all_controls, pheno] = 0

    return output_pheno

EUR_counts = pd.read_table('Sampling/cluster_counts_nhw', sep=' ', index_col='pheno')['count']
EUR_pheno = pd.read_table('Sampling/w-endo_W_covariates.txt', sep=' ')
EUR_out = pd.DataFrame(index=EUR_pheno.index, columns=list(range(1, 6)))
EUR_out['endometriosis'] = EUR_pheno['STATUS']

EUR_out = do_sampling(EUR_counts, EUR_out)
print(EUR_out.apply(lambda x: x.value_counts()).transpose())
EUR_out.index.name = 'IID'
EUR_out.to_csv('Sampling/EUR_pheno.csv')

AFR_counts = pd.read_table('Sampling/cluster_counts_nhb', sep=' ', index_col='pheno')['count']
AFR_pheno = pd.read_table('Sampling/w-endo_NHB_covariates.txt', sep=' ')
AFR_out = pd.DataFrame(index=AFR_pheno.index, columns=list(range(1, 6)))
AFR_out['endometriosis'] = AFR_pheno['STATUS']

AFR_out = do_sampling(AFR_counts, AFR_out)
print(AFR_out.apply(lambda x: x.value_counts()).transpose())
AFR_out.index.name = 'IID'
AFR_out.to_csv('Sampling/AFR_pheno.csv')

