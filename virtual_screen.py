import pandas as pd
import tools.extract as extract
import tools.transform as transform
import pipeline.protein_cleaning as protein_cleaning

arthritis_data = 'data/fasta/arthritis.fasta'
cardiovascular_data = 'data/fasta/cardiovascular.fasta'
cytokine_data = 'data/fasta/cytokine.fasta'
disease_data = 'data/fasta/disease.fasta'
inflammation_data = 'data/fasta/inflammation.fasta'

drug_data = 'data/csv/cann_mols.csv'



clean_proteins = (protein_df.
                 pipe(info_parser).
                 pipe(info_pre_processed).
                 pipe(info_processed_disease))