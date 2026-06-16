valores = [10, 20, 30]

# i vai de 0 ate 2
for i in range (len(valores)):
    # Multiplicando cada elemento pela sua posição
    valores[i] = valores[i] * i

print(valores) # Saida: [0, 20, 60]
