import matplotlib.pyplot as plt

produtos=["Mouse","Teclado","Monitor"]
precos=[35, 80, 700]

plt.barras(produtos, precos)
plt.title("Preços de produtos")
plt.show()

#o matplotlib não reconhece a função "Barras" o correto é bar