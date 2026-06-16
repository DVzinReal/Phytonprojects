# Davi Marinho Donato

tabuleiro = [
    [0, 0, 1, 0, 2, 0, 0],
    [0, 1, 1, 0, 2, 2, 0],
    [0, 0, 1, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 1, 0, 0, 0],
    [0, 2, 2, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
]

#a) Exibir tabuleiro de forma gráfica
def exibir(tab):
    '''
    Exibe o tabuleiro com:
    - Números das colunas (0 a 6) na primeira linha
    - Número da linha no início de cada linha
    - '.' para vazio, 'X' para preto (1), 'O' para branco (2)
    '''
    print("0 1 2 3 4 5 6")               # cabeçalho das colunas
    for joguin, linha in enumerate(tab): # joguin = índice da linha
        print(joguin, end="")            # número da linha
        for val in linha:
            if val == 0:
                print(".", end=" ")
            elif val == 1:
                print("X", end=" ")
            else:                        # val == 2
                print("O", end=" ")
        print()                          # quebra de linha após cada linha

exibir(tabuleiro)

#b) Contagem de peças
# Achata a lista 2D em uma lista 1D (compreensão aninhada)
tudim = [v for linha in tabuleiro for v in linha]

pretas = tudim.count(1)
brancas = tudim.count(2)
vazias = tudim.count(0)

print("Pretas:", pretas)
print("Brancas:", brancas)
print("Vazias:", vazias)

#c) Listar vizinhos (cima, baixo, esquerda, direita)
def vizinhos(tab, joguin, jogao):
    '''
    Retorna uma lista com os valores dos vizinhos ortogonais da posição (joguin, jogao).
    Ignora posições que estariam fora do tabuleiro (índices 0 a 6).
    '''
    res = []

    if joguin > 0:                      # vizinho de cima
        res.append(tab[joguin - 1][jogao])
    if joguin < 6:                      # vizinho de baixo
        res.append(tab[joguin + 1][jogao])
    if jogao > 0:                       # vizinho da esquerda
        res.append(tab[joguin][jogao - 1])
    if jogao < 6:                       # vizinho da direita
        res.append(tab[joguin][jogao + 1])

    return res

print(vizinhos(tabuleiro, 0, 0))   # canto superior esquerdo
print(vizinhos(tabuleiro, 3, 3))   # centro
print(vizinhos(tabuleiro, 6, 6))   # canto inferior direito

#d) Espelhamento horizontal
# Inverte a ordem dos elementos dentro de cada linha
tabuleiro_espelho = [linha[::-1] for linha in tabuleiro]

exibir(tabuleiro_espelho)

#e) Transposição (trocar linhas por colunas)
tabuleiro_transposto = [
    [tabuleiro[jogao][joguin] for jogao in range(7)]
    for joguin in range(7)
]

# Verifica se um elemento específico foi transposto corretamente
print(tabuleiro[2][5] == tabuleiro_transposto[5][2])


