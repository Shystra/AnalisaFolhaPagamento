import pandas as pd;

from trata_dados_contemSalario import trata_df_contemSalario;
from trata_dados_folha import trata_df_folha;

caminho_contemSalario = r"C:\Users\Shystra\Documents\Testes\ContémSalario.xlsx"
caminho_folha = r"C:\Users\Shystra\Documents\Testes\INTERSEPT SEGURANCA LTDA 072023.xlsx"

df_contemSalario = trata_df_contemSalario(caminho_contemSalario)
df_folha = trata_df_folha(caminho_folha)

# Antes do ajuste
vigilantes_com_periculosidade = df_contemSalario[df_contemSalario['Nome Função'].str.contains('Vigilante|Tático', case=False) & (df_contemSalario['% Periculosidade'] == 30)]
print(vigilantes_com_periculosidade[['Nome Função', 'Salário']].head())

# Faça o ajuste
df_contemSalario = ajusta_salario_vigilantes_com_periculosidade(df_contemSalario)

# Depois do ajuste
print(vigilantes_com_periculosidade[['Nome Função', 'Salário']].head())


# Continue com o código que não pertence a nenhuma das funções
print(df_contemSalario['Nome Função'].value_counts())
print(df_contemSalario['Desc. Situação'].value_counts())
print(df_contemSalario['% Insalubridade'].value_counts())
print(df_contemSalario['% Periculosidade'].value_counts())
print(df_contemSalario[['Nome Função', 'Salário']].head())

