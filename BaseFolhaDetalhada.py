import pandas as pd
from trata_dados_folha import trata_df_folha;

caminho_folha = r"C:\Users\Shystra\Documents\Testes\INTERSEPT SEGURANCA LTDA 072023.xlsx"

df_folha = trata_df_folha(caminho_folha)
df_folha, total_por_funcionario = trata_df_folha(caminho_folha)

print(total_por_funcionario)











# # Visão geral dos dados
# print(df_folha.head())

# # Fornece estatisticas media, mediana e minima
# print(df_folha.describe())

# # Mostra a quantidade de valores ausentes (NaN)
# print(df_folha.isnull().sum())

# # Garante os tipos corretos das colunas
# print(df_folha.dtypes)

# # Identifica diversidade de valores em uma coluna
# print(df_folha['Nome Ocorrência'].value_counts())


