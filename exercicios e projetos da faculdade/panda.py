import pandas as pd
# Criando uma tabela de dados
dados = {"Nome": ["Ana", "Bruno", "Carlos"], "idade": [25, 30, 22]}
df = pd.DataFrame(dados)
#mostrar tabelas
print(df)
#filtrar pessoas com idade > 24
maiores = df[df["idade"] > 24]