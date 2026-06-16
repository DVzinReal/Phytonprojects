 # Criando variaveis em Python
nome = "dracula"
# str
idade = 234
# int
altura = 1.90
# float
estudante = True #arte das trevas
# bool


x = 100
# x e um inteiro
x = "Java"
# Agora x e uma string


a = b = c = 1000 # Todas terao o mesmo valor

a = 3
d = 6
b = 21313
c = 453


idade = 34
_contador = 0
nome_completo = "Pedro"
Usuario1 = "caba"
CONSTANTE = 3.14
nome = "jão"
altura = 1.60
e_estudante = True

nome = "Pedro"
# Nao pode comecar com numero
nome-completo = "seila"
# Nao pode conter hifen
#for = 10
# Nao pode ser palavra reservada

from math import pi
print(pi)

 # Ou
import math
pi = math.pi
print(pi)

RODAPE = "Curso de Python"

from math import pi

numero_inteiro = 3
numero_float = 0.5

#Conversão entre Tipos Numéricos
preco = 10
print(preco)
# 10

preco = float(preco)
print(preco)
# 10.0

preco = 10 / 2
print(preco)
# 5.0

preco = 10.30
print(preco)
# 10.3

preco = int(preco)
print(preco)
# 10

nome = "Python"
mensagem = "Ola, mundo!"
texto_longo = """Este e um texto
que ocupa varias
linhas."""

texto = "python e incrivel"
print("o texto e", texto) # o texto e python e incrivel
print(texto.upper()) # PYTHON E INCRIVEL
print(texto.capitalize()) # Python e incrivel
print(texto.replace("e", "e muito")) # python e muito incrivel
print(texto.split()) # [’python’, ’e’, ’incrivel’]
print(len(texto)) # 17 (comprimento da string)

nome = "Python"
sobrenome = "Programming"

# Concatenacao
nome_completo = nome + " " + sobrenome # "Python Programming"
print(nome_completo)

# Repeticao
repetir = nome * 3 # "PythonPythonPython"
print(repetir)

# Indexacao (acessando caracteres individuais)
primeira_letra = nome[0] # "P"
print(primeira_letra)
ultima_letra = nome[-1] # "n"
print(ultima_letra)

 # Fatiamento (slicing)-obtendo partes da string
tres_primeiras = nome[0:3] # "Pyt"
print(tres_primeiras)
ultimas_letras = nome[-3:] # "hon"
print(ultimas_letras)

maior_de_idade = True
tem_desconto = False
python_e_facil = True
terra_e_plana = False

# Operacoes logicas
resultado1 = python_e_facil and terra_e_plana # False
resultado2 = python_e_facil or terra_e_plana # True
resultado3 = not terra_e_plana # True

 # Valores que sao considerados False:
print(bool(0))
# False- zero inteiro
print(bool(0.0))
# False- zero flutuante
print(bool(""))
# False- string vazia
print(bool([]))
# False- lista vazia
print(bool({}))
print(bool(None))

print(bool(1))
print(bool(-1))
# False- dicionario vazio
# False- valor None
# Todos os outros valores sao considerados True:
# True- inteiro nao-zero
# True- inteiro negativo
print(bool("False")) # True- string nao-vazia
print(bool([0]))
# True- lista nao-vazia

#Manipulação de Listas
frutas = ["maca", "laranja", "uva", "pera"]
frutas[0]
# maca
frutas[2]
# uva
frutas[-1]
# pera
frutas[-3]
# laranja

matriz = [



]
[1, "a", 2],
["b", 3, 4],
[6, 5, "c"]
matriz[0]
# [1, "a", 2]
matriz[0][0]
# 1
matriz[0][-1]
# 2
matriz[-1][-1] # "c"

frutas = ["maca", "banana", "laranja"]

# Acessando elementos
primeira_fruta = frutas[0] # "maca"
print(primeira_fruta)

# Modificando elementos
frutas[1] = "morango" # ["maca", "morango", "laranja"]
print(frutas)

# Adicionando elementos
frutas.append("uva") # Adiciona ao final
frutas.insert(1, "pera") # Insere na posicao 1
print(frutas)

# Removendo elementos
frutas.remove("maca") # Remove pelo valor
ultima_fruta = frutas.pop() # Remove e retorna o ultimo item
print(frutas)

carros = ["gol", "celta", "palio"]
for modelos in carros:
    print(modelos)




#Tuplas são sequências ordenadas e imutáveis de elementos.
coordenadas = (10, 20) # tupla com 2 elementos
cores_rgb = (255, 0, 0) # tupla com 3 elementos
singleton = (42,) # tupla com 1 elemento (virgula necessaria)

# Acessando elementos (semelhante as listas)
x = coordenadas[0] # 10
y = coordenadas[1] # 20

# Diferentemente das listas, nao podemos modificar elementos:
# coordenadas[0] = 15 # Isso geraria um erro!

# Desempacotamento de tuplas
r, g, b = cores_rgb # r=255, g=0, b=0


#Dicionários
pessoa = {"nome": "Ana", "idade": 30, "profissao": "Engenheira"}
config = {"debug": True, "max_connections": 100}

# Acessando valores
nome = pessoa["nome"] # "Ana"
print(nome)

# Metodo seguro para acessar (nao gera erro se a chave nao existir)
email = pessoa.get("email", "nao informado") # "nao informado"
print(email)

# Adicionando ou modificando valores
pessoa["email"] = "ana@exemplo.com"
print(pessoa["email"])
pessoa["idade"] = 31
print(pessoa["idade"])

#Dicionários
pessoa = {"nome": "Ana", "idade": 30, "profissao": "Engenheira"}
config = {"debug": True, "max_connections": 100}

# Acessando valores
nome = pessoa["nome"] # "Ana"
print(nome)

# Metodo seguro para acessar (nao gera erro se a chave nao existir)
email = pessoa.get("email", "nao informado") # "nao informado"
print(email)

# Adicionando ou modificando valores
pessoa["email"] = "ana@exemplo.com"
print(pessoa["email"])
pessoa["idade"] = 31
print(pessoa["idade"])

# Verificando a existencia de uma chave
if "idade" in pessoa:
    print("Idade encontrada!")

# Removendo valores
del pessoa["profissao"]
print(pessoa)

# Iterando sobre o dicionario
for chave in pessoa:
    print(f"{chave}: {pessoa[chave]}")

# Obtendo chaves e valores
todas_chaves = pessoa.keys()
print(todas_chaves)
todos_valores = pessoa.values()
print(todos_valores)

preco = 10.50
idade = 28
print(str(preco)) # 10.5
print(str(idade)) # 28

texto = f"idade {idade} preco {preco}"
print(texto) # idade 28 preco 10.5



#Conjuntos(set)
vogais = {"a", "e", "i", "o"}
numeros_primos = {2, 3, 5, 7, 11, 13}


# Nao permite elementos duplicados
letras = {"a", "b", "a", "c"} # Sera {"a", "b", "c"}
print(letras)

# Adicionando elementos
vogais.add("y")
print(vogais)

# Removendo elementos
vogais.remove("y")
print(vogais)




#Operações de Conjuntos
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

uniao = conjunto1 | conjunto2 # {1, 2, 3, 4, 5, 6}
print(uniao)

intersecao = conjunto1 & conjunto2 # {3, 4}
print(intersecao)

diferenca = conjunto1- conjunto2 # {1, 2}
print(diferenca)

diferenca_simetrica = conjunto1 ^ conjunto2 # {1, 2, 5, 6}
print(diferenca_simetrica)

#None é um valor nulo
 # None e frequentemente usado para inicializar variaveis
resultado = None

# Verificando se uma variavel e None
if resultado is None: # Use ’is’ em vez de ’==’
    print("Ainda nao temos um resultado")

# Funcoes que nao retornam valor explicitamente retornam None
def funcao_sem_retorno():
    print("Esta funcao nao retorna nada explicitamente")

valor = funcao_sem_retorno()
print(valor) # Imprime: None

# Calculando a media de dois numeros
a = 5
b = 8
media = (a + b) / 2
print("A media e =", media)

#Conversão entre Tipos de Dados

#Convertendo string para inteiro e realizando soma
numero_str = "10"
numero_int = int(numero_str)
soma = numero_int + 5
print("O resultado da soma e:", soma)
# Saida: O resultado da soma e: 15

#Criando uma saudação personalizada
nome = "Ana"
saudacao = "Ola, " + nome + "! Bem-vinda ao Python."
print(saudacao)
# Saida: Ola, Ana! Bem-vinda ao Python.

#Adicionando itens a uma lista e calculando a soma
numero = [2, 4, 6, 8]
numero.append(10)
print(numero)
# [2, 4, 6, 8, 10]

soma = sum(numero)
print(soma)
# 30

# Operadores Lógicos e de Comparação
a = 10
b = 5
print(a == b) # False
print(a != b) # True
print(a > b)
# True
print(a < b)
# False
print(a >= b) # True
print(a <= b) # False

#Operadores Lógicos

a = 10; b = 3

resultado_and = (a > 5) and (b < 5) # True
print(resultado_and)

resultado_or = (a > 15) or (b < 5)
# True
print(resultado_or)

resultado_not = not (a > 5)
# False
print(resultado_not)

# Operadores logicos com booleanos
x = True
y = False
print(x and y) # False
print(x or y)
# True
print(not x)
# False

saldo = 450
saque = 200
print(saldo == saque) # False

curso = "Curso de Python"
frutas = ["laranja", "uva", "limao"]
saques = [1500, 200]

print("Python" in curso)
# True
print("maca" not in frutas)
# True
print(200 in saques)
# True
print(1500 not in saques)
# False
'''
input() Entrada de dados
print() Mostra na tela
len() Tamanho dos conteúdos
type() Verifica o tipo
range() Criar sequências de números
append() Adicionando dados a uma lista
sum() Soma os elementos de uma lista
max() / min() Retorna o maior/menor valor
sorted() Retorna uma lista ordenada
enumerate() Retorna índice ao percorrer listas
zip() Agrupa elementos de várias listas em pares
'''

#Entrada de Dados – input()
nome = input (" Digite seu nome : ")
idade = int( input (" Digite sua idade : ") )
data_nascimento = int( input (" Digite sua data_nascimento : ") )

print ( nome )
print ( idade )
print ( data_nascimento )


nome = input ("Por favor , digite o seu nome : ")
print ("Ola , " + nome )

#Tipos de Dados
idade = 20 # tipo int
nota_final = 8.75 # tipo float
nome_aluno = " Joana Silva " # tipo str
aprovado = True # tipo bool

# Impressao dos tipos
print ( type ( idade ) ) # <class ’int ’>
print ( type ( nota_final ) ) # <class ’float ’>
print ( type ( nome_aluno ) ) # <class ’str ’>
print ( type ( aprovado ) ) # <class ’bool ’>

idade_aluno = 23
nota_final = 7.2
nome_aluno = "Richard cavalo marinho"
media_final = aprovado

print(type(idade_aluno))
print(type(nota_final))
print(type(nome_aluno))
print(type(media_final))


#f-Strings
nome = " Maria "
idade = 20
print ( f"{ nome } tem { idade } anos .")

preco = " 10.50 "
idade = "28"
print ( float ( preco ) ) # 10.5
print ( int ( idade ) ) # 28

#Formatação com % (estilo antigo)

nome = " Marcia "
idade = 46
profissao = " professora "
linguagem = " Python "

print ("Ola , me chamo %s. Eu tenho %s anos de idade , trabalho como %s eestou matriculado no curso de %s." % ( nome , idade , profissao ,linguagem))

#Formatação com .format()
print ("Ola , me chamo {}. Eu tenho {} anos de idade , trabalho como {} eestou matriculado no curso de {}. ". format ( nome , idade , profissao ,linguagem ))

print ("Ola , me chamo {3}. Eu tenho {2} anos de idade , trabalho como {1}e estou matriculado no curso de {0}. ". format ( linguagem , profissao ,idade , nome ))

print ("Ola , me chamo { nome }. Eu tenho { idade } anos de idade , trabalhocomo { profissao } e estou matriculado no curso de { linguagem }.". format( nome = nome , idade = idade , profissao = profissao , linguagem = linguagem ))

#Fatiamento de Strings
nome = " Marcia Ramos Luiz "

nome [0] # ’M’
nome [1] # ’a’
nome [:9] # ’Marcia Ra ’
nome [10:] # ’mos Luiz ’
nome [10:16] # ’mos Lu ’
nome [10:16:2] # ’msL ’
nome [:] # ’Marcia Ramos Luiz ’
nome [:: -1] # ’ziuL somaR aicraM ’

print ( nome [:])
print ( nome [:: -1])

#Range
for num in range (3) :
    print("Head First Rocks !")

# Saida :
# Head First Rocks!
# Head First Rocks!
# Head First Rocks!

#atividade final
nome = "João"
idade = 25

print(f"meu nome é {nome} e eu tenho {idade} anos")


nome_curso = str(input("Digite o nome do curso: "))
duracao_curso = float(input("Digite a duração: "))

semestres = duracao_curso / 100

print(f"o seu curso {nome_curso} tem uma carga horaria de {duracao_curso} e tem {semestres} semestres.")