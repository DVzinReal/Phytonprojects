# Davi Marinho Donato


texto_original = "a sorte esta lancada e o rubicao foi cruzado"
mensagem_cifrada = "n hzcal lhao yhujhkh l v cyfpjhv mvp jybchkv"

#a) Função cifrar (Cifra de César)
def cifrar(texto, chave):
    '''
    Aplica deslocamento 'chave' no alfabeto (a=0, b=1, ..., z=25).
    Espaços são mantidos inalterados.
    '''
    resultado = ""

    for letra in texto:
        if letra == " ":
            resultado += letra                     # preserva espaços
        else:
            # Converte letra para número (0-25), soma chave, módulo 26, volta a caractere
            resultado += chr((ord(letra) - ord('a') + chave) % 26 + ord('a'))

    return resultado

#b) Quebra automática por heurística de espaços
# Tenta todas as 26 chaves possíveis e escolhe a que gera mais espaços no texto decifrado
melhor_chave = 0
melhor_texto = ""

for a in range(26):
    # Para decifrar, aplica deslocamento complementar (26 - chave)
    texto_tentativa = cifrar(mensagem_cifrada, 26 - a)

    # Critério simples: quanto mais espaços, mais provável ser texto legível
    if texto_tentativa.count(" ") > melhor_texto.count(" "):
        melhor_texto = texto_tentativa
        melhor_chave = a

print("Chave encontrada:", melhor_chave)
print("Texto decifrado:", melhor_texto)

#c) Função para contar frequência de letras
def frequencia(texto):
    '''
    Retorna um dicionário onde chave = letra, valor = número de ocorrências.
    Ignora espaços.
    '''
    freq = {}

    for letra in texto:
        if letra == " ":
            continue
        freq[letra] = freq.get(letra, 0) + 1   # get com padrão 0 evita KeyError

    return freq

# Calcula frequência na mensagem cifrada
freq_cifrada = frequencia(mensagem_cifrada)

# Pega as 5 letras mais frequentes
top5 = sorted(freq_cifrada.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 letras mais frequentes:")
for letra, contagem in top5:
    print(f"{letra} {contagem}")

#d) Tentativa de decifrar baseada nas letras mais frequentes
# Para cada letra do top5, supõe que ela corresponda ao 'e' (letra mais comum em português)
# e calcula a chave correspondente, depois tenta decifrar
for letra, _ in top5:
    chave = (ord(letra) - ord('a'))          # posição da letra no alfabeto (0-25)
    print(chave, cifrar(mensagem_cifrada, 26 - chave))

#e) Histograma de frequência do texto original
freq_original = frequencia(texto_original)

# Ordena do mais frequente para o menos frequente
ordenado = sorted(freq_original.items(), key=lambda x: x[1], reverse=True)

print("\nHistograma")
for letra, contagem in ordenado:
    print(f"{letra} | {'#' * contagem} {contagem}")

