numeros = [1, 2, 3, 4, 5]

quadrados = [n**2 for n in numeros]

pares = [n for n in numeros if n % 2 == 0]

pares_quadrado = [n**2 for n in numeros if n % 2 == 0]

identidade = [
    [1 if i == j else 0 for j in range(5)]
    for i in range(5)
]

print(quadrados)
print(pares)
print(pares_quadrado)

for linha in identidade:
    print(linha)