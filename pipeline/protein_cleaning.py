import pandas as pd

def prepare_targets(dfx):
    drug_data = pd.read_csv('cann_mols.csv')  
    df_targets = dfx[['Protein name','sequence']]# making a copy of the clean dataframe.
    target_name = df_targets['Protein name'].tolist()
    target = df_targets.sequence.tolist()
    drug_name = drug_data.Name.tolist()
    drug = drug_data.SMILES.tolist()

    return target_name, target, drug_name, drug