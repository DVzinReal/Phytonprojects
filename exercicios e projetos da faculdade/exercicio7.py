import pandas as pd #o pandas cria e manipula as tabelas       #python -m pip install pandas 
import seaborn as sns #faz gráficos bonitos                    #python -m pip install seaborn matplotlib
import matplotlib.pyplot as plt  #controla o gráfico (título, eixos, etc.)

#isto abaixo e um dicionario
dados = {                                      
    "titulo": ["O iluminado", "Megamente", "Angry birds"], #cada chave e uma coluna 
    "genero": ["terror", "comedia", "comedia"],            #cada lista e um valor da coluna
    "ano": [1980, 2010, 2016],
    "nota_de_avaliacao": ["84%", "70%", "44%"]
}

df = pd.DataFrame(dados) #aqui e onde os dados viram uma tabela
#fica tipo um excel

#converter nota
df["nota_de_avaliacao"] = df["nota_de_avaliacao"].str.replace("%","").astype(int) #df seleciona a coluna e o str.replace tira o %
#df = seleciona a coluna 
#str.replace = tira o %
#astype(int) = transforma de texto pra numero

#grafico
sns.barplot(x="titulo", y="nota_de_avaliacao", data=df)
#x=""titulo" = coloca os nomes em um eixo horizontal
#y= nota de avaliacao = coloca os valores em eixo vertical
#data=df = é de onde vem os dados

plt.title("Avaliação de filmes ou séries") #coloca um titulo no grafico
plt.xlabel("Título") #da nome pros eixos
plt.ylabel("Nota (%)") #tambem da nome pros eixos 
plt.xticks(rotation=45) #gira os nomes 

plt.tight_layout()  # ajusta o espaçamento para que não fique nada cortado pra fora da tela
plt.show() #exibe o grafico na tela 