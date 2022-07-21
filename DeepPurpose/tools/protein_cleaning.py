import pandas as pd

def create_drug_target_pairs(targets, drug_data):
    
    
    targets['drug_name'] = drug_data['Name'][0]
    targets['SMILES'] = drug_data['SMILES'][0]

    df_targets_2 = targets.copy()
    df_targets_2['drug_name'] = drug_data['Name'][1]
    df_targets_2['SMILES'] = drug_data['SMILES'][1]

    df_targets_3 = targets.copy()
    df_targets_3['drug_name'] = drug_data['Name'][2]
    df_targets_3['SMILES'] = drug_data['SMILES'][2]

    df_targets_4 = targets.copy()
    df_targets_4['drug_name'] = drug_data['Name'][3]
    df_targets_4['SMILES'] = drug_data['SMILES'][3]

    df_targets_5 = targets.copy()
    df_targets_5['drug_name'] = drug_data['Name'][4]
    df_targets_5['SMILES'] = drug_data['SMILES'][4]

    df_targets_6 = targets.copy()
    df_targets_6['drug_name'] = drug_data['Name'][5]
    df_targets_6['SMILES'] = drug_data['SMILES'][5]

    df_targets_7 = targets.copy()
    df_targets_7['drug_name'] = drug_data['Name'][6]
    df_targets_7['SMILES'] = drug_data['SMILES'][6]

    df_targets_8 = targets.copy()
    df_targets_8['drug_name'] = drug_data['Name'][7]
    df_targets_8['SMILES'] = drug_data['SMILES'][7]

    df_targets_9 = targets.copy()
    df_targets_9['drug_name'] = drug_data['Name'][8]
    df_targets_9['SMILES'] = drug_data['SMILES'][8]

    all_targets = pd.concat([targets, 
                  df_targets_2, 
                  df_targets_3, 
                  df_targets_4, 
                  df_targets_5, 
                  df_targets_6, 
                  df_targets_7, 
                  df_targets_8, 
                  df_targets_9], axis=0)
                  

    return all_targets

def make_lists(targets):
    target_name = targets['id'].tolist()
    target = targets.sequence.tolist()
    drug_name = targets.drug_name.tolist()
    drug = targets.SMILES.tolist()
    
    return drug, target, drug_name, target_name