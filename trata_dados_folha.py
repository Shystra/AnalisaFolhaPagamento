# Aqui vão as operações de tratamento para df_folha

import pandas as pd

def trata_df_folha(caminho):
    df = pd.read_excel(caminho)
    
    # Remove linhas completamente vazias
    df = df.dropna(how='all')

    # Remove linhas que contem os dados da primeira coluna
    df = df[df.index != df[df.columns[0]].eq(df.columns[0]).idxmax()]

     # Remoção da coluna 'Unidade Adm. (Cliente)'
    if 'Unidade Adm. (Cliente)' in df.columns:
        df.drop(columns=['Unidade Adm. (Cliente)'], inplace=True)
    


    # Conversao das colunas de datas
    df['Data Valor Inicial'] = pd.to_datetime(df['Data Valor Inicial'], dayfirst=True, errors='coerce')
    df['Data Valor Final'] = pd.to_datetime(df['Data Valor Final'], dayfirst=True, errors='coerce')



    # Conversao das colunas para númerico
    colunas_para_numeric = ['Unidade1', 'Unidade2', 'Valor']
    for col in colunas_para_numeric:
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        except Exception as e:
            print(f"Erro encontrado ao tentar converter a coluna '{col}': {e}")







    df = df[df['Categoria'].isin(['Desconto', 'Provento'])]
    # Aplicação de Desconto vs Provento
    df['Valor'] = df.apply(lambda x: -x['Valor'] if x['Categoria'] == 'Desconto' else x['Valor'], axis=1)
    
    


    # Concatena nome e matricula
    df['Nome_Matricula'] = df['Nome'] + "-" + df['Matrícula'].astype(str) 


    # Somatório por funcionario
    total_por_funcionario = df.groupby('Nome_Matricula')['Valor'].sum().reset_index()




    # print(df.head())  # Primeiras linhas do dataframe
    # print("\nInformações do DataFrame:\n")
    # print(df.info())  # Resumo das colunas, dados não nulos e tipos de dados

    return df, total_por_funcionario
