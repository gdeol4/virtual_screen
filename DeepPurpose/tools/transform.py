import pandas as pd

def string_splitter(string):
    string = string.split("HUMAN",1)[1]
    string = string.split("OS=Homo sapiens")
    
    return string

def info_pre_processed(dfx):
    df = dfx.copy() # create a copy of df
    list_of_info = list(dfx['info']) # convert column values to list
    list_of_info = [string_splitter(x) for x in list_of_info] # apply string_splitter function to list elements
    df['temp_col'] = list_of_info # create a temporary column from the processed list
    df.drop("info", axis=1, inplace=True) # drop info column
    split_df = pd.DataFrame(df['temp_col'].tolist(), columns=['Protein name', 'info']) # creating this dataframe to merge back onto processed dataframe
    df.drop("temp_col", axis=1, inplace=True) # dropping temp_col
    df = pd.concat([df, split_df], axis=1) # merging both dataframes

    return df

def info_processed_cyto_arth(dfx, protein_df):
    df = dfx.copy() # create a copy of the dataframe
    split_df = df['info'].str.split(' ', expand=True) # creating a seperate dataframe to merge with
    df = pd.concat([df, split_df], axis=1) # merge dataframes
    df.drop("info", axis=1, inplace=True) # drop info column
    df.columns = ['type', 'id', 'Protein name', 'drop', 'Species', 'Gene', 'PE', 'Mutation', 'v1', 'v2', 'v3'] # rename columns
    df.drop(["v1", 'v2', 'v3' ], axis=1, inplace=True) # drop empty column
    df = pd.concat([df, protein_df], axis=1) # merge dataframes
    df.drop("info", axis=1, inplace=True) # drop info column
    df.drop('Species', axis=1, inplace=True) # drop column
    df['Gene'] = df['Gene'].str[3:] # strip first 3 characters
    
    return df

def info_processed_cardio_inflam(dfx, protein_df):
    df = dfx.copy() # create a copy of the dataframe
    split_df = df['info'].str.split(' ', expand=True) # creating a seperate dataframe to merge with
    df = pd.concat([df, split_df], axis=1) # merge dataframes
    df.drop("info", axis=1, inplace=True) # drop info column
    df.columns = ['type', 'id', 'Protein name', 'drop', 'Species', 'Gene', 'PE', 'Mutation'] # rename columns
    #df.drop(["v1", 'v2', 'v3' ], axis=1, inplace=True) # drop empty column
    df = pd.concat([df, protein_df], axis=1) # merge dataframes
    df.drop("info", axis=1, inplace=True) # drop info column
    df.drop('Species', axis=1, inplace=True) # drop column
    df['Gene'] = df['Gene'].str[3:] # strip first 3 characters
    
    return df

def info_processed_disease(dfx, protein_df):
    df = dfx.copy() # create a copy of the dataframe
    split_df = df['info'].str.split(' ', expand=True) # creating a seperate dataframe to merge with
    df = pd.concat([df, split_df], axis=1) # merge dataframes
    df.drop("info", axis=1, inplace=True) # drop info column
    df.columns = ['type', 'id', 'Protein name', 'drop', 'Species', 'Gene', 'PE', 'Mutation', 'v1', 'v2'] # rename columns
    df.drop(["v1", 'v2'], axis=1, inplace=True) # drop empty column
    df = pd.concat([df, protein_df], axis=1) # merge dataframes
    df.drop("info", axis=1, inplace=True) # drop info column
    df.drop('Species', axis=1, inplace=True) # drop column
    df['Gene'] = df['Gene'].str[3:] # strip first 3 characters
    
    return df