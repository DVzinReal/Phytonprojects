letras = ['a', 'b', 'c', 'd', 'e', 'f']
#do indice 1 ao 3, (o 4 não entra)
print(letras[1:4]) #['b', 'c', 'd']
#Do inicio ate ao indice 2
print(letras[:3])
#Do indice 3 ate ao fim
print(letras[3:])

# Copia completa da lista (Copia independente na memoria)
copia = letras[:]