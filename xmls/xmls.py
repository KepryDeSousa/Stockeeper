import pandas as pd

Banco_load = pd.read_excel('xmls/Efas_para_fazer.xlsx', index_col=0)
Banco_load2 = pd.read_excel('xmls/Efas_para_fazer.xlsx', index_col=0, sheet_name='Planilha2')
print(Banco_load.head())
print(Banco_load2.head())

dt = pd.merge(Banco_load, Banco_load2, on='Loja', how='inner')
print(dt.head())