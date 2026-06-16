# importa a biblioteca statistics, usada para fazer cálculos estatísticos
import statistics

# lista com os tempos de download em segundos
tempos = [12.5, 10.8, 14.2, 9.9, 11.7, 13.1, 10.5]

# statistics.mean() calcula a média dos valores da lista
# round(valor, 2) serve para arredondar o resultado para 2 casas decimais
media = round(statistics.mean(tempos), 2)

# statistics.median() calcula a mediana (valor central da lista em ordem)
# round(valor, 2) arredonda para 2 casas decimais
mediana = round(statistics.median(tempos), 2)

# statistics.stdev() calcula o desvio padrão dos valores
# round(valor, 2) arredonda para 2 casas decimais
desvio_padrao = round(statistics.stdev(tempos), 2)

# max() encontra o maior valor da lista
maior_tempo = max(tempos)

# min() encontra o menor valor da lista
menor_tempo = min(tempos)

# print() mostra os resultados na tela
print("Média:", media)
print("Mediana:", mediana)
print("Desvio padrão:", desvio_padrao)
print("Maior tempo:", maior_tempo)
print("Menor tempo:", menor_tempo)