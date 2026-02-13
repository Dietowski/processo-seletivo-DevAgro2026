<h1 align=center>Processo Seletivo - DevAgro2026</h1>

<h3 align=center>O projeto foi desenvolvido para um teste técnico, que teve como objetivo implementar um processador de movimentações financeiras, realizando diversos cálculos e análises de dados.</h3>

<hr>

## Índice
* [Instruções](#instruções)
* [Base de dados](#base-de-dados)
* [Etapas](#etapas)
* [Funcionalidades Principais](#funcionalidades-principais)

<hr>

## Instruções
<p><b>Linguagem:</b> Python 3.13.12</p>
<p><b>Biblioteca utilizada:</b> Pandas<br></p>
<h2>Como usar:</h2>
<ol>
  <li><b>Primeiro passo:</b> Instale o Python na versão descrita anteriormente, link: <i>https://www.python.org/downloads/</i></li>
  <li><b>Segundo passo:</b> Instale a biblioteca Pandas:</li>
    <ul>
      <li>Vá no terminal e digite: <i>pip install pandas</i></li>
    </ul>
  <li><b>Terceiro passo:</b> Novamente, vá ao terminal e use o comando git clone <i>'url do repositório'</i> para baixar os arquivos do projeto.</li>
  <li><b>Quarto passo:</b> Certifique-se de que está na pasta códigos e abra o terminal, use o comando: <i>python3 leitor_arquivos_csv.py</i></li>
</ol>

<hr>

## Base de dados
<p align=center>A base de dados é a mesma usada como exemplo para o desafio, porém com informações adicionais para auxiliar nas etapas.</p>


| data       | conta        | tipo | valor   | descrição            |
|------------|--------------|------|---------|----------------------|
| 2026-01-01 | CAIXA        | C    | 1000.00 | Saldo inicial        |
| 2026-01-01 | BANCO BRASIL | C    | 5000.00 | Aporte Capital       |
| 2026-01-01 | SANTANDER    | C    | 2000.00 | Empréstimo           |
| 2026-01-02 | CAIXA        | D    | 150.50  | Compra de Papelaria  |
| 2026-01-02 | BANCO BRASIL | D    | 100.00  | Tarifa Manutenção    |
| 2026-01-03 | SANTANDER    | D    | 500.00  | Pagamento Aluguel    |
| 2026-01-04 | CAIXA        | D    | 900.00  | Retirada Sócios      |
| 2026-01-05 | BANCO BRASIL | C    | 1500.00 | Venda a Vista        |
| 2026-01-05 | BANCO BRASIL | C    | 1500.00 | Venda a Vista        |
| 2026-01-06 | AMERICA      | C    | 300.00  | Venda Pequena        |
| 2026-01-06 | ZURICH       | C    | 1000.00 | Seguro               |
| 2026-01-07 | CAIXA        | C    | 2000.00 | Reposição de Caixa   |
| 2026-01-08 | SANTANDER    | D    | 2500.00 | Pagamento Fornecedor |
| 2026-01-09 | BANCO BRASIL | D    | 50.00   | Taxa TED             |
| 2026-01-10 | CAIXA        | D    | 50.00   | Lanche Equipe        |

<hr>

## Etapas
<ol>
  <li><b>Etapa 1:</b> Ler o arquivo CSV, calcular o saldo final por conta (crédito soma, débito subtrai) e exibir o resultado em ordem alfabética.</li>
  <li><b>Etapa 2:</b> Calcular totais de créditos, débitos e quantidade de lançamentos. Processar os registros na ordem do arquivo e registrar inconsistências quando o saldo ficar negativo em qualquer momento do processamento.</li>
  <li><b>Etapa 3:</b> Implementar fechamento diário por conta e detectar lançamentos duplicados quando todos os campos forem idênticos.</li>
</ol>
<p>Vale ressaltar que a <b>Etapa 4</b> que foi descrita como bônus técnico, não foi concluída por fatores técnicos e conhecimentos avançados para o autor.</p>

<hr>

## Funcionalidades Principais
<ul>
  <li><b>Leitura de arquivo csv:</b> Carrega o arquivo CSV, converte os valores para formato numérico e transforma lançamentos de "Débito" (D) em valores negativos para o cálculo corrigido</li>

  <li><b>Cálcllo de saldo final:</b> Agrupa os dados por conta bancária para apresentar o saldo total consolidado.</li>

  <li><b>Resumo de lançamentos:</b> Gera um relatório contendo o total de créditos, o total de débitos e a contagem de lançamentos para cada conta.</li>

  <li><b>Monitoramento de saldo negativo:</b> Calcula o saldo acumulado linha a linha para verificar e alertar se a conta ficou negativa em algum momento específico.</li>

  <li><b>Fechamento diário:</b> Agrupa as movimentações por data para demonstrar o saldo total movimentado em cada dia.</li>

  <li><b>Verificação de duplicidade:</b> Identifica se existem linhas duplicadas na base de dados e imprime quais são elas.</li>
  </ul>
