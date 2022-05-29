## Comprehensive prediction of robust synthetic lethality between paralog pairs in cancer cell lines
Data processing and analysis code for the paper of the same name, published in *Cell Systems*: [https://doi.org/10.1101/2020.12.16.423022](https://doi.org/10.1016/j.cels.2021.08.006)

Cite as: De Kegel *et al.* (2021) Comprehensive prediction of robust synthetic lethality between paralog pairs in cancer cell lines. *Cell Systems*

Supplementary data and all SHAP profiles are available at: http://www.cancergd.org/static/paralogs/

### Data analysis notebooks overview:
All the main and supplementary figures and statistics for the manuscript are generated in these notebooks.

| Notebook                               | Figures                 | Brief description                                        |
|:---------------------------------------|:------------------------|:---------------------------------------------------------|
| 01_compare_GI_screens                  | Fig. 1, S1              | Investigate bias and cell line specific hits in existing combinatorial screens |
| 02_identify_paralog_SLs_w_DepMap       | Fig. 2                  | Derive our dataset of robust SL paralog pairs (training data)                  |
| 03_indiv_feature_analysis              | Fig. 3A, S2, S3         | Investigate the indv. predictive power of 22 features of paralog pairs |
| 04_train_classifier                    | Fig. 3B                 | Cross-validation of random forest classifier w/ our training data |
| 05_validate_classifier                 | Fig. 4A, S4, S5         | Validate classifier with combinatorial screen results |
| 06_make_predictions                    | Fig. 4B, 5A             | Make predictions for all paralog pairs |
| 07_explain_predictions                 | Fig. 5B,C,D, 6A,C,E, S8 | Generate SHAP profiles for indv. predictions |
| 08_compare_other_classifiers           | Fig. S6                 | Compare performance of RF predictions to that of SLant predictions |
| 09_experimental_validation             | Fig. 6D,F               | Graph siRNA screen results for *ASF1A/ASF1B* and *COPS7A/COPS7B* |
| 10_human_vs_cerevisiae_paralogs        | NA                      | Compare the avg. family size for paralogs in humans vs. cerevisiae yeast |
| 11_gene_loss_in_tcga                   | Fig. 6B                 | Homozygous deletions frequency of *ASF1A* and *COPS7B* in TCGA |
| 12_test_robustness_of_classifier       | Fig. S7                 | Evaluate robustness of the classifier’s performance and rankings |


### Data processing notebooks overview:
These notebooks process raw/third party data for use in the analysis.

| Notebook                               | Brief description                                        |
|:---------------------------------------|:---------------------------------------------------------|
| 01_process_hgnc_id_map                 | Create map with HGNC symbol, Entrez ID, Ensembl ID and locus type (e.g. protein-coding) for each gene |
| 02_process_ensembl_paralogs            | Generate list of protein-coding paralog pairs with min. 20% sequence identity + some feat. annotations |
| 03_process_copy_number                 | Identify homozygous deletions from copy number and gene expression data |
| paralog_features/01_process_protein_complexes | Compute protein complex membership and essentiality features for paralog pairs |
| paralog_features/02_process_ppi        | Compute protein-protein interaction features for paralog pairs  |
| paralog_features/03_process_orthologs  | Identify (essential) orthologs for paralog pairs and compute conservation score |
| paralog_features/04_process_gtex_expression   | Compute expression features for paralog pairs |
| paralog_features/05_merge_all_features | Generate full list of all paralog pairs annotated with all features - some features, incl. age, are computed in this notebook |
| GI_screens/process_thompson_pairs      | Process gene pairs screened by Thompson et al.  |
| GI_screens/process_dede_pairs          | Process gene pairs screened by Dede et al.     |
| GI_screens/process_parrish_pairs       | Process gene pairs screened by Parrish et al.     |
| GI_screens/process_chymera_pairs       | Process gene pairs screened by Gonatopoulos-Pournatzis et al.  |

### Running CERES overview:
These notebooks + R scripts are used to re-process logfold change data from DepMap CRISPR screens with [CERES](https://github.com/cancerdatasci/ceres), to remove multi-targetting sgRNAs. The output from running all scripts in this folder is available as `local_data\processed\depmap20Q2\gene_scores_16_04_21.csv` (and similar for Sanger screens). The notebooks can run in the conda environment, but the R scripts should be run independently (e.g. in R studio). Code to install the necessary Bioconductor packages + CERES is included in the R scripts. The R scripts also require the [bowtie](http://bowtie-bio.sourceforge.net/index.shtml) and [samtools](http://samtools.sourceforge.net/) command line tools which are only available for Linux/macOS.

| Order | Notebook or R scripts                  | Brief description                                        |
|:------|:---------------------------------------|:---------------------------------------------------------|
|1      | 01_preprocess_depmap_data              | Extract sgRNAs to align and format files for CERES       |
|2      | R_scripts/align_guides.R               | Align all sgRNAs to the reference genome (hg38), allowing up to two mismatches |
|3      | 02_filter_multi_target_guides          | Filter out sgRNAs that align to readthrough genes and/or to multiple protein-coding genes (incl. w/ mismatch) |
|4      | R_scripts/run_CERES.R                  | Run CERES with the filtered logfold changes data |
|5      | 03_ceres_post_processing               | Process CERES output to drop genes targeted by too few guides + normalize scores to reference (non-)essential genes |


### To run Jupyter notebooks:
* Obtain 3rd party data - sources are listed in data_sources
   * The folder for running CERES has its own data_sources file with the third party files that are only needed there
   * Note: this is primarily needed for running notebooks in the 1_data_processing folder
* Set path to 3rd party data directory in environment.yml (3rd_party_dir)
  * Note: this can also be set in the activate environment with: `conda env config vars set 3rd_party_data=my_dir`
* Create [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) environment from the environment.yml file: `conda env create -f environment.yml`
* Activate conda environment: `conda activate paralogSL`
* Start notebooks: `jupyter notebook`




