dia = int(input("Quanto dias ficou com o carro?: "))
km = float(input("Quantos km rodou com o carro?: "))
dia_preco = dia * 60
km_preco = km * 0.15
total = dia_preco + km_preco
print(f"Você ficou com o carro por {dia} dias oque custou {dia_preco} e rodou por {km} kilometros custando {km_preco} que custou no total  {total}")

