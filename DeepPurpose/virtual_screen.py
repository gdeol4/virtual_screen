import pandas as pd
import tools.extract as extract
import tools.transform as transform
import tools.protein_cleaning as pipeline
from DeepPurpose import DTI as models

#read in data
arthritis_data = 'data/fasta/arthritis.fasta'
cardiovascular_data = 'data/fasta/cardiovascular.fasta'
cytokine_data = 'data/fasta/cytokine.fasta'
disease_data = 'data/fasta/disease.fasta'
inflammation_data = 'data/fasta/inflammation.fasta'
drug_data = pd.read_csv('data/csv/cann_mols.csv')

# change dataset here
protein_df = extract.loading_fasta(arthritis_data)

# produce model ready protein set
clean_proteins = (protein_df.
                 pipe(extract.info_parser).
                 pipe(transform.info_pre_processed).
                 pipe(transform.info_processed_cyto_arth, protein_df))

# subset dataframe
clean_proteins = clean_proteins[['id','sequence']]

#create dataset with all drug target pairs
targets = pipeline.create_drug_target_pairs(clean_proteins, drug_data)

#extract lists
targets = pipeline.make_lists(targets)

# chose model
net = models.model_pretrained(model = 'Daylight_AAC_BindingDB_IC50')

# perform virtual screen
_ = models.virtual_screening(targets[0], targets[1], net, targets[2], targets[3])

