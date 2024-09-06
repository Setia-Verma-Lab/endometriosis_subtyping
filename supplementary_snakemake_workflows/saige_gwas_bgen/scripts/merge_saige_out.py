import os
import pandas as pd
import argparse as ap
import sys

TEST_ROWS = None
TEST_CHR = None

def buildArgs():
    parser = ap.ArgumentParser()

    parser.add_argument('-r', '--results', metavar='Dir/', help='Directory with chromosome-wise results .txt files', default='Saige_Step2_Results/')
    parser.add_argument('--info', metavar='Min INFO', help='Minimum imputation INFO score when merging', default=0.3, type=float)
    parser.add_argument('--cols', metavar='ColNames.txt', help='File with 2 columns (no header): column 1 = Regenie column name, column 2 = Output column name')
    parser.add_argument('--pheno', metavar='phenotype-name')
    parser.add_argument('-o', '--out')

    return parser

def writeOutput(df, filename):
    df.to_csv(filename, index=False, sep='\t', na_rep='NA')

args = buildArgs().parse_args()
pheno = args.pheno

resultsFiles = os.listdir(args.results)
resultsFiles = [args.results + f for f in resultsFiles if '.txt' == f[-4:]]

colMap = pd.read_table(args.cols, header=None, sep='\s+', index_col=0).to_dict()[1]

files = [f for f in resultsFiles if 'bin.' + pheno + '.' in f or 'quant.' + pheno  + '.' in f]

print('Merging results for', pheno)
dfs = []
for f in files[:TEST_CHR]:
    print(f)
    temp = pd.read_table(f, sep='\s+', nrows=TEST_ROWS)
    temp['CHR'] = temp['CHR'].astype(str).str.replace('chr', '')
    dfs.append(temp)
    print('\t', len(temp), 'SNPs read from', f, flush=True)

df = pd.concat(dfs)
print(df.columns)

print('Sorting by CHR and POS')
df = df.sort_values(by=['CHR', 'POS'])
df = df.rename(columns=colMap)

print(len(df), 'Total SNPs.')
print('Writing to Sumstats...', flush=True)
df.to_csv(args.out, index=False, sep='\t', na_rep='NA')

print('Done')