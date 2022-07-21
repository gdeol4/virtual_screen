import pandas as pd
import pandas as pd
from Bio.SeqIO.FastaIO import SimpleFastaParser

def loading_fasta(fasta_file):
    fasta = open(fasta_file)
    fasta_list = list(SimpleFastaParser(fasta))

    return pd.DataFrame(fasta_list, columns=['info', 'sequence'])

def info_parser(dfx):
    df = dfx.copy()
    df = df['info'].str.split('|', expand=True) # split on the "|" character
    df.columns = ['type', 'id', 'info'] # rename the three columns # rename the three columns

    return df

def info_parser_200k(dfx):
    df = dfx.copy()
    df = df['info'].str.split('|', expand=True) # split on the "|" character
    df.columns = ['type', 'id', 'info', 'none'] # rename the three columns # rename the three columns
    df.drop("none", axis=1, inplace=True) # drop info column

    return df
