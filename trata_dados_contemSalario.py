# Lidará com operações relacionadas ao DataFram 'df_contemSalario'
import pandas as pd

def trata_df_contemSalario(caminho_contemSalario):
    df = pd.read_excel(caminho_contemSalario)
    
    df = df[df['Nome'] != 'Nome']
    df.reset_index(drop=True, inplace=True)

    # Concatenando e Criando valores Unicos
    df['chave'] = df['Nome'] + "-" + df['Matrícula'].astype(str)
    # Remover linhas com valores NaN na coluna 'chave'
    df = df.dropna(subset=['chave'])
    
    # Verificar novamente as duplicatas após a remoção
    duplicadas_apos_remocao = df[df.duplicated(subset='chave', keep=False)]
    if not duplicadas_apos_remocao.empty:
        print("Duplicatas ainda presentes:")
    else:
        print("Nenhuma duplicata encontrada na coluna chave após a remoção.")

    try:
        df['Salário'] = pd.to_numeric(df['Salário'])
    except Exception as e:
        print(f"Erro encontrado: {e}")

    try: 
        df['Jornada Mensal Horas'] = pd.to_numeric(df['Jornada Mensal Horas'])
    except Exception as e:
        print(f"Erro encontrado ao tentar converter a coluna 'Jornada Mensal Horas': {e}")

    df = ajusta_salario_vigilantes_com_periculosidade(df)
    
    return df

def ajusta_salario_vigilantes_com_periculosidade(df):
    # Máscara para identificar registros de 'Vigilantes' e 'Táticos' com 30% de periculosidade
    mascara = df['Nome Função'].str.contains('Vigilante|Tático', case=False) & (df['% Periculosidade'] == 30)

    # Calcular o adicional de 30% sobre o salário base
    df.loc[mascara, 'Salário'] = df.loc[mascara, 'Salário'] * 1.30

    return df
