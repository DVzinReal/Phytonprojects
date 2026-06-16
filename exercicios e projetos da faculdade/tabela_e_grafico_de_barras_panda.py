import pandas as pd
import matplotlib.pyplot as plt

# criando uma tabela de dados
dados = {
    "Produto": ["Arroz", "Feijão",
    "Macarrão", "Açúcar", "Café"],
    "Preço": [20.50, 12.30, 8.90, 5.75, 18.00]
}

df = pd.DataFrame(dados)

#mostrando a tabela 
print("Tabela de produtos:\n")
print(df)

#fazendo um gráfico de barras
plt.bar(df["Produto"], df["Preço"])
plt.title("Preços dos Produtos")
plt.xlabel("Produtos")
plt.ylabel("Preço (R$)")
plt.show()