#Importando as funções que foram criadas no arquivo auxiliar utils.py, que representa utilitário.
from utils import *

#Caminho da base de dados armazenada em uma pasta dedicada.
caminho_csv = "../arquivos/dados_teste.csv"

try:
    #               ETAPA 1
    #Lê o arquivo csv e armazena a tabela na variável "tabela"
    tabela = ler_arquivo(caminho_csv)
    
    #Cria uma nova coluna que recebe os valores da forma em que: C = positivo(positivo), D = negativo(subtrai), axis=1 representa o eixo
    tabela['valor_corrigido'] = tabela.apply(calcular_valor_corrigido, axis=1)

    #A função utiliza uma tabela que soma a coluna de valor_ajustado para cada tipo de conta bancária,
    #depois essa nova tabela será armazenada na variável "saldo_final"
    saldo_final = calcular_saldo_final(tabela)
    print(saldo_final)

    #               ETAPA 2
    #A função reutiliza a tabela, reorganizando a coluna e os indíces para gerar uma nova tabela com a soma dos valores de crédito,
    #débito e a contagem dos lançamentos. A função retorna uma tabela que será armazenada na variável "total".
    total = calcular_lancamentos(tabela)
    print(total)

    #A função cria uma nova coluna chamada saldo_acumulado, em que para cada conta, será calculado a soma dos valores acumulativamente,
    #mostrando quando fica negativo ou não.
    tabela_registros = registrar_inconsistencias(tabela)
    print(tabela_registros)
    #A função do tipo void, verifica se há saldos negativos em qualquer momento da soma acumulativa, caso tenha, a função própria mostra
    #as linhas em que houve essa questão.
    processar_saldos_negativos(tabela_registros)
    
    #               ETAPA 3
    #A função agrupa as datas em dia (baseado na frequência) por valores que foram corrigidos, assim tendo a soma total por dia. 
    tabela_fechamento_diario = fechamento_diario(tabela)
    print(tabela_fechamento_diario)
    
    #Função void que apenas verifica se houve lançamentos repetidos, a própria função realiza a impressão caso tenha duplicação, mostrando as linhas de
    #ocorrência.
    detectar_lancamento_duplicado(tabela)

except FileNotFoundError:
    print("Caminho não encontrado")