#import csv
#
#with open('../arquivos/dados_teste.csv', "r") as arquivo:
#    arquivo_csv = csv.reader(arquivo, delimiter=";")
#    for linha in arquivo_csv:
#        print(linha)

from utils import *

caminho_csv = "../arquivos/dados_teste.csv"

tabela = ler_arquivo(caminho_csv)
caminho_excel = "../arquivos/dados_excel.xlsx"

tabela['valor_ajustado'] = tabela.apply(calcular_valor_ajustado, axis=1)
saldo_total = tabela.groupby('conta').agg(
    saldo_total = ('valor_ajustado', 'sum')
    ).sort_index()

print(saldo_total)

#               TESTES DE APRENDIZADO
#tabela.to_excel(caminho_excel, index=False)
#print(tabela["valor"].sum()) #ou display no jupyter notebook
##tabela["valor_acumulado"] = tabela["valor"] * 12
##tabela.drop('valor', axis=1)
#print(tabela.info())
#print(tabela.describe())
#print(tabela.sort_values(by="conta", ascending=False)) OU SEM ASCENDING PRA FICAR DO MENOR PRO MAIOR
#print(tabela["conta"].value_counts())
#print(tabela.groupby("conta")["valor"].mean())

##tabela['valor_ajustado'] = tabela['valor']
##tabela.loc[tabela['tipo'] == 'D', 'valor_ajustado'] *= -1