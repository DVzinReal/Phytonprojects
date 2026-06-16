import seaborn as sns
import matplotlib.pyplot as plt

#lista de consumos
consumos = [3, 7, 12, 5, 9, 15, 4]
dias = ["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5", "Dia 6", "Dia 7"]
#Cálculos
total = sum(consumos)
media = total / len(consumos)
maior = max(consumos)
menor = min(consumos)

print("Total: ", total)
print("Média: ", media)
print("Maior consumo:", maior)
print("menor consumo:", menor)

#classificação e cores
classificacao = []
cores = []


for consumo in consumos:
    if consumo < 5:
        classificacao.append("baixo")
        cores.append("green")
    elif 5 <= consumo <= 10:
        classificacao.append("moderado")
        cores.append("orange")
    else:
        classificacao.append("alto")
        cores.append("red")

#mostrar classificação
for i in range(len(consumos)):
    print(f"Dia {i+1}: {consumos[i]} GB - {classificacao[i]}")

#4 Gráfico com seaborn
sns.set(style="whitegrid")

plt.figure(figsize=(8,5))
sns.barplot(x=dias, y=consumos, palette=cores)

plt.title("Consumo de internet por Dia")
plt.xlabel("Dias")
plt.ylabel("Consumo (GB)")

plt.show()
