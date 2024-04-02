import yfinance

# Vamos obter valores das Ações
# Necessário incluir a ação
# Quero saber
# 1 Cotação mínima da ação
# 2 Cotação máxima da ação
# 3 Cotação do dia

codAção = input("Digite o código da ação - EX: PETR4.SA, VALE3.SA, ELET6.SA, BBAS3.SA :")

dados = yfinance.Ticker(codAção)

dados.history()

# Período de 1 ano para ação
tabela = dados.history("1y")
tabela

# Preço de fechamento
fechamento = tabela.Close
fechamento


# Valores Máxima, Minima e valor Atual
maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento.iloc[-1]


print(f'Cotação máxima no período é R$ {round(maxima, 2)}\n')
print(f'Cotação minima no período é R$ {round(minima, 2)}\n')
print(f'Cotação atual da ação é R$ {round(atual, 2)}\n')