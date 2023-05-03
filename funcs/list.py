import pandas as pd

# define o número máximo de colunas a serem exibidas
pd.options.display.max_columns = 999

# define a largura do console
pd.options.display.width = 1000

# lê a planilha
df = pd.read_excel('cadFun.xlsx')

# exibe todos as colunas
print(df)