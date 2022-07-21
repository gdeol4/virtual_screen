import pandas as pd
from DeepPurpose import DTI as models
targets = pd.read_csv(r'./Data/csv/disease_targets.csv')
df_drugs = pd.read_csv('cann_mols.csv') 

targets['drug_name'] = df_drugs['Name'][0]
targets['SMILES'] = df_drugs['SMILES'][0]

df_targets_2 = targets.copy()
df_targets_2['drug_name'] = df_drugs['Name'][1]
df_targets_2['SMILES'] = df_drugs['SMILES'][1]

df_targets_3 = targets.copy()
df_targets_3['drug_name'] = df_drugs['Name'][2]
df_targets_3['SMILES'] = df_drugs['SMILES'][2]

df_targets_4 = targets.copy()
df_targets_4['drug_name'] = df_drugs['Name'][3]
df_targets_4['SMILES'] = df_drugs['SMILES'][3]

df_targets_5 = targets.copy()
df_targets_5['drug_name'] = df_drugs['Name'][4]
df_targets_5['SMILES'] = df_drugs['SMILES'][4]

df_targets_6 = targets.copy()
df_targets_6['drug_name'] = df_drugs['Name'][5]
df_targets_6['SMILES'] = df_drugs['SMILES'][5]

df_targets_7 = targets.copy()
df_targets_7['drug_name'] = df_drugs['Name'][6]
df_targets_7['SMILES'] = df_drugs['SMILES'][6]

df_targets_8 = targets.copy()
df_targets_8['drug_name'] = df_drugs['Name'][7]
df_targets_8['SMILES'] = df_drugs['SMILES'][7]

df_targets_9 = targets.copy()
df_targets_9['drug_name'] = df_drugs['Name'][8]
df_targets_9['SMILES'] = df_drugs['SMILES'][8]

dfxx = pd.concat([targets, 
                  df_targets_2, 
                  df_targets_3, 
                  df_targets_4, 
                  df_targets_5, 
                  df_targets_6, 
                  df_targets_7, 
                  df_targets_8, 
                  df_targets_9], axis=0)

dfxx.to_csv('disease_clean.csv')

target_name = dfxx['Protein name'].tolist()
target = dfxx.sequence.tolist()
drug_name = dfxx.drug_name.tolist()
drug = dfxx.SMILES.tolist()

# Virtual screening using the trained model or pre-trained model 

net = models.model_pretrained(model = 'MPNN_CNN_BindingDB')

_ = models.virtual_screening(drug, target, net, drug_name, target_name)