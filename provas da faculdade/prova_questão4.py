# Davi Marinho Donato

catalogo = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "genero": "romance", "paginas": 256},
    {"titulo": "O Processo", "autor": "Franz Kafka", "ano": 1925, "genero": "romance", "paginas": 304},
    {"titulo": "Cem Anos de Solidao", "autor": "Gabriel Garcia Marquez", "ano": 1967, "genero": "romance", "paginas": 448},
    {"titulo": "Ficcoes", "autor": "Jorge Luis Borges", "ano": 1944, "genero": "contos", "paginas": 174},
    {"titulo": "A Metamorfose", "autor": "Franz Kafka", "ano": 1915, "genero": "novela", "paginas": 96},
    {"titulo": "O Aleph", "autor": "Jorge Luis Borges", "ano": 1949, "genero": "contos", "paginas": 196},
    {"titulo": "Memorias Postumas", "autor": "Machado de Assis", "ano": 1881, "genero": "romance", "paginas": 208},
    {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977, "genero": "novela", "paginas": 87},
    {"titulo": "Rayuela", "autor": "Julio Cortazar", "ano": 1963, "genero": "romance", "paginas": 600},
    {"titulo": "A Paixao Segundo G.H.", "autor": "Clarice Lispector", "ano": 1964, "genero": "romance", "paginas": 179},
]

#a) Busca por campo exato
def buscar(catalogo, campo, valor):
    '''
    Retorna uma lista com todos os livros onde livro[campo] == valor.
    Exemplo: buscar(catalogo, "autor", "Franz Kafka")
    '''
    return [livro for livro in catalogo if livro[campo] == valor]

print(buscar(catalogo, "autor", "Franz Kafka"))
print(buscar(catalogo, "genero", "contos"))

#b) Ordenação por campo
def ordenar_por(catalogo, campo, decrescente=False):
    '''
    Ordena o catálogo de acordo com o valor de 'campo' em cada livro.
    Se decrescente = True, ordena do maior para o menor.
    '''
    return sorted(catalogo, key=lambda x: x[campo], reverse=decrescente)

print(ordenar_por(catalogo, "ano"))           # ordena do mais antigo ao mais novo
print(ordenar_por(catalogo, "paginas", True)) # ordena do mais longo ao mais curto

#c) Estatísticas gerais
def estatisticas(catalogo):
    '''
    Calcula:
    - total de livros
    - média de páginas (arredondada para 2 casas)
    - título do livro mais antigo
    - título do livro mais recente
    '''
    total = len(catalogo)

    # Soma das páginas de todos os livros, dividida pelo total
    media_paginas = sum(o["paginas"] for o in catalogo) / total

    # min/max com key=lambda x: x["ano"] encontra o livro com menor/maior ano
    mais_antigo = min(catalogo, key=lambda x: x["ano"])["titulo"]
    mais_recente = max(catalogo, key=lambda x: x["ano"])["titulo"]

    return {
        "total": total,
        "media_das_pagina": round(media_paginas, 2),
        "mais_antigo": mais_antigo,
        "mais_recente": mais_recente
    }

print(estatisticas(catalogo))

#d) Agrupar livros por autor
def agrupar_por_autor(catalogo):
    '''
    Retorna um dicionário onde:
    chave = nome do autor
    valor = lista de títulos dos livros desse autor
    '''
    autores = {}

    for livro in catalogo:
        autor = livro["autor"]
        # setdefault: se autor não existe, cria com lista vazia; depois adiciona título
        autores.setdefault(autor, []).append(livro["titulo"])

    return autores

grupos = agrupar_por_autor(catalogo)

# Exibe apenas autores que têm mais de um livro no catálogo
for autor, livros in grupos.items():
    if len(livros) > 1:
        print(autor, livros)

#e) Filtrar por intervalo de anos
def filtrar_intervalo(catalogo, ano_ini, ano_fim):
    '''
    Retorna uma lista com os livros cujo ano está entre ano_ini e ano_fim (inclusive).
    '''
    return [
        livro for livro in catalogo
        if ano_ini <= livro["ano"] <= ano_fim
    ]

resultado = filtrar_intervalo(catalogo, 1940, 1970)

for livro in resultado:
    print(livro["titulo"], livro["ano"])