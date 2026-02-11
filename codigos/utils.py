import pandas as pd

def ler_arquivo(caminho:str):
    tabela = pd.read_csv(caminho, sep=";")
    tabela["valor"] = pd.to_numeric(tabela["valor"], errors="coerce") #garante que a coluna valor tenha apenas números, se tiver um valor que não é, ele será considerado Not a Number
    return tabela

def calcular_valor_ajustado(linha):
    if linha['tipo'] == 'D':
        return linha['valor'] * -1
    else:
        return linha['valor'] * 1