import random

# Lista dos grupos
grupos = [
    "GRUPO 1 - Ana Helloyse",
    "GRUPO 2 - Francisco Gonçalves",
    "GRUPO 3 - Emely",
    "GRUPO 4 - João Victor",
    "GRUPO 5 - Lucas",
    "GRUPO 6 - Johnata Ruan",
    "GRUPO 7 - Davi Marinho",
    "GRUPO 8 - João Emanuel"
]

# Embaralhar os grupos
random.shuffle(grupos)

# Mostrar ordem sorteada
print("🎲 Ordem de Apresentação:\n")

for i, grupo in enumerate(grupos, start=1):
    print(f"{i}. {grupo}")