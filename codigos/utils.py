import pandas as pd

def ler_arquivo(caminho:str):
    #Função do pandas para ler arquivo csv, o separador utilizado é o mesmo dos dados passados como exemplo
    tabela = pd.read_csv(caminho, sep=";")
    
    #Garante que a coluna valor tenha apenas números, se tiver um valor que não é, ele será considerado Not a Number
    tabela["valor"] = pd.to_numeric(tabela["valor"], errors="coerce")
    
    #Apaga uma coluna que foi criada após definir que na coluna valor tenha apenas números
    tabela = tabela.drop(columns=['Unnamed: 5'], errors='ignore')
    return tabela

def calcular_valor_corrigido(coluna):
    if coluna['tipo'] == 'D':
        #ajusta para quando for débito o valor fique negativo, assim nas somas totais ele será considerado uma subtração
        return coluna['valor'] * -1
    else:
        return coluna['valor'] * 1

def calcular_saldo_final(tabela):
    #Agregando de forma que adicione um nome na coluna, chamado "saldo_final", somando os valores de valor_ajustado em relação a conta
    #Por fim, ordenando os valores de forma crescente baseando no nome das contas
    saldo_final = tabela.groupby('conta').agg(
    saldo_final = ('valor_corrigido', 'sum')
    ).sort_values(by='conta')
    
    return saldo_final

def calcular_lancamentos(tabela):
    #"Pivotando" a tabela, transformando a conta em indíce e as colunas foram separadas de acordo com o tipo("C" ou "D"),
    #por fim elas foram somadas baseado no indíce que são as contas
    total = tabela.pivot_table(index='conta', columns='tipo', values='valor', aggfunc='sum', fill_value=0)
    
    #Dando nome para as colunas, pois até então são separas apenas como o tipo.
    total.columns = ['Total dos créditos', 'Total dos débitos']
    
    #Criando uma nova coluna para a quantidade de lançamentos que irá conter o número de lançamentos de cada conta.
    #O cálculo é feito baseado no nome das contas, para este caso é importante que não tenha nomes iguais para contas diferentes
    total['Lancamentos por conta'] = tabela['conta'].value_counts()
    
    return total

def registrar_inconsistencias(tabela):
    #Criando uma tabela auxiliar que recebe a cópia da tabela original. O porquê disso se dá pois estava tendo conflitos na etapa 3
    #que calcula os lançamentos repetidos, porém como o cumsum soma acumulativamente, as linhas deixavam de ser iguais.
    tabela_aux = tabela.copy()
    #Método que soma acumulativamente, agrupando o valor_corrigido com as contas e colocando o valor na nova coluna
    tabela_aux['saldo_acumulado'] = tabela_aux.groupby('conta')['valor_corrigido'].cumsum()
    
    return tabela_aux

def processar_saldos_negativos(tabela):
    #Filtra os valores que no saldo acumulativo ficou negativo em determinado momento, isso no caso vai gerar um DataFrame com as linhas em que
    #o valor da coluna ficou negativo
    saldos_negativos = tabela[tabela['saldo_acumulado'] < 0]
    #Comparação se o DataFrame é vazio, se a comparação for falsa é porque não está vazia e imprime os resultados
    if saldos_negativos.empty == False:
        print(f"\nSaldos negativos:\n{saldos_negativos}")
    else:
        print("Não possui saldos negativos")

def fechamento_diario(tabela):
    #Conversão do tipo de dados da coluna data para o formato datetime. Conforme foi utilizado no exemplo, a formatação é: Ano-mês-dia,
    #como no desafio técnico foi citado que seriam usados dados no mesmo formato, permaneceu neste formato.
    tabela['data'] = pd.to_datetime(tabela['data'], format='%Y-%m-%d')
    
    #Agrupa a soma dos valores corrigidos com a coluna de data, porém, ela que agrupada com o Grouper, pois foi usado o argumento freq para
    #que a frequência seja diária como foi pedido. Poderia ser M de mês ou W para semanas.
    tabela_fechamento_diario = tabela.groupby(pd.Grouper(key='data', freq='D')).agg(
        saldo_diario = ('valor_corrigido', 'sum')
    )
    
    return tabela_fechamento_diario

def detectar_lancamento_duplicado(tabela):
    #verifica se na tabela há linhas duplicadas, o método duplicated retorna uma Series booleana e o método any retorna True se houver True
    if tabela.duplicated().any() == True:
        #A variável linha duplicada recebe a tabela filtrada com as linhas duplicadas, apenas são passadas as linhas True, ou seja, duplicadas.
        linha_duplicada = tabela[tabela.duplicated()]
        print(f"Existe duplicacação(ões) na(s) linha(s): \n{linha_duplicada}")
    else:
        print("Não há lançamentos duplicados nesta base de dados.\n")