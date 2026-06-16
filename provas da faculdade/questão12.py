produtos = [
    {"nome": "Mouse", "preco": 80},
    {"nome": "Teclado", "preco": 150},
    {"nome": "Monitor", "preco": 1200},
    {"nome": "Notebook", "preco": 3500}
]

def buscar_produto(produtos, nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return produto
    return None

def mais_caro(produtos):
    return max(produtos, key=lambda p: p["preco"])

def media_precos(produtos):
    soma = sum(p["preco"] for p in produtos)
    return soma / len(produtos)

print(buscar_produto(produtos, "Monitor"))
print(mais_caro(produtos))
print(media_precos(produtos))