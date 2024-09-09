# Introduction

This is the order of commands to replicate the analyses performed. 

Any time I'm running `snakemake all`, the pertinent output files are listed under `rule all` in the respective `Snakefile` of that directory.

Many of the `Snakefile`s have `include:` statements at the top. Source code for those dependency Snakemake pipelines can be found in `supplementary_snakemake_workflows`

The exact python environment is described in `py11.yml`. To replicate this environment, do:
- `mamba env create -f py311.yml`

# Genotype Preparation
## `Locus_Extraction`

The code in this sub-directory takes the Rahmioglu lead SNPs and creates BED files that have a 500kb window on other side (in both build 37 and build 38)

- `snakemake all`

## `1KG_LD_Testing`

Within the 500kb windows from the previous section, we use 1KG to find LD tag SNPs for each GWAS lead SNP. SNPs were considered tag SNPs if the R2 was at least 0.1

- `snakemake all`

# Cluster Preparation
## `Cluster_Training`
This section details how we defined the clusters using endometriosis cases from the non-genotyped PMBB.

- Make sure that Feature_Extraction/config_pheno.yaml is up to date
- `snakemake Pheno/FULL_PMBB_all_cleaned_phenos.csv`
- Notebook: `construct_input_data_no_snps_full_PMBB.ipynb`
- Notebook: `cluster_method_testing.ipynb` <- Figure 1
- Notebook: `cluster_training_spectral_k5.ipynb` <- Assigns clusters and Creates Model Pickle
- Notebook: `spectral_clustering_vis.ipynb` <- Figure 2
- Notebook: `endo_subtype_cluster_tests.ipynb` <- Figures 3 and 4

## `Feature_Extraction`

This is where we extract the EHR features for the other three local datasets (PMBB, eMERGE, and UKBB). Also, this is where we examine the input feature prevalence among the datasets.

- `snakemake all`
- Notebook: `get_dataset_prevalences.ipynb` <- Figure S2

# Candidate Gene Association Testing
## `Association_Testing`

In this top directory we first collect all of the phenotype and sample size information

- `snakemake all` <- Tables 1 and 2

Then in each sub-directory for PMBB, eMERGE, and UKBB, we do:
- `snakemake sample_size_table.csv`
- `snakemake all`

For AOU, I uploaded the tarball summary stats downloaded from the workbench and ran the following scripts:
- `bash make_sumstats_dirs.sh`
- `python get_aou_sample_sizes_from_sumstats.py`

For BioVU, I was able to copy the summary stats from Box:
- `bash rclone_copy_from_box.sh`
- `bash link_box_sumstats.sh`
- `snakemake all` (I had to do some post-processing and help James Jaworski with the random sampling for the negative control)

## `Association_Testing_Negative_Control`
- Handled the same way as the previous section, excludes the overall endometriosis phenotype

# Meta-Analyses
## `Meta_Analysis`

Here, we use `plink --meta` to meta-analyze the effects from the individual studies.

- `snakemake all` <- prepares input files
- Notebook: `Perform_Meta_Analysis.ipynb`

## `Meta_Analysis_Negative_Control`
Same as previous section

# Examining Cluster Genetic Heterogeneity
## `Cluster_Heterogeneity`

Looking at genetic differences between the clusters, incorporating information from the positive and negative controls

- Notebook: `Test_Cluster_Heterogeneity.ipynb` <- Figures 5 and 6

