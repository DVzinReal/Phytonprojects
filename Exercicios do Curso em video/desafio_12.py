preco = float(input("Digite o preço do produto: R$ "))
desconto = preco * 0.05
novo_preco =  preco - desconto

print(f"O preço era {preco} com desconto é: {novo_preco:.2f}")