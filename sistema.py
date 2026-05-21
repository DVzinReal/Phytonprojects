# importa a biblioteca sqlite3 para criar e manipular banco de dados SQL
import sqlite3 as sql

# importa a biblioteca random para gerar números aleatórios
import random

# importa Faker para gerar dados falsos aleatórios
from faker import Faker

# importa pandas para criar DataFrames
import pandas as pd

# importa csv para criar arquivos CSV
import csv

# importa Workbook para criar planilhas Excel
from openpyxl import Workbook

# importa biblioteca para criar arquivos XML
import xml.etree.ElementTree as ET


# permite mostrar todas as colunas do DataFrame no terminal
pd.set_option('display.max_columns', None)

# define o idioma dos dados falsos como português do Brasil
fake = Faker("PT-Br")


# cria/conecta ao banco de dados SQLite
conexao = sql.connect("registros.db")

# cria cursor responsável pelos comandos SQL
cursor = conexao.cursor()


# remove a tabela antiga caso ela já exista
cursor.execute("DROP TABLE IF EXISTS registros")


# cria a tabela registros
cursor.execute("""
CREATE TABLE IF NOT EXISTS registros(
    ID INTEGER PRIMARY KEY,
    Nome,
    Email,
    Idade,
    Endereco,
    Nota
)
""")


# lista temporária usada para armazenar os dados
aluno = []


# pergunta quantos registros serão criados
registros = int(input("Quantos registros precisam ser criados? "))


# função responsável por gerar registros aleatórios
def gerar_registros():

    # repete o processo conforme a quantidade escolhida
    for num in range(1, registros + 1):

        # adiciona ID
        aluno.append(num)

        # adiciona nome aleatório
        aluno.append(fake.name())

        # adiciona email aleatório
        aluno.append(fake.email())

        # adiciona idade aleatória
        aluno.append(random.randint(18, 60))

        # adiciona endereço aleatório
        aluno.append(fake.address())

        # adiciona nota aleatória
        aluno.append(random.randrange(7, 11))


        # insere os dados na tabela SQL
        cursor.execute(
            "INSERT INTO registros VALUES(?,?,?,?,?,?)",
            aluno
        )

        # limpa a lista para reutilização
        aluno.clear()


    # salva definitivamente os dados no banco
    conexao.commit()


# executa a função
gerar_registros()


# função responsável por mostrar DataFrame
def mostrar_dataFrame():

    # lê os dados da tabela SQL
    df = pd.read_sql_query("SELECT * FROM registros", conexao)

    # mostra os dados no terminal
    print(df)


# executa a função
mostrar_dataFrame()


# Parte 3 - Criando arquivo CSV
def salvar_csv():

    """
    Salva todos os registros do banco SQL
    em um arquivo CSV.
    """

    # busca todos os dados da tabela
    dados = cursor.execute("SELECT * FROM registros").fetchall()


    # cria/abre o arquivo CSV
    with open("registros.csv", mode="w", newline="", encoding="utf-8") as arquivo:

        # cria objeto de escrita CSV
        escritor = csv.writer(arquivo)

        # escreve o cabeçalho
        escritor.writerow(["ID", "Nome", "Email", "Idade", "Endereço", "Nota"])

        # escreve todos os registros
        escritor.writerows(dados)


    print("\nArquivo 'registros.csv' criado com sucesso!")


# função para ler o arquivo CSV
def ler_csv():

    print("===== LEITURA DO ARQUIVO CSV =====")

    # abre o arquivo CSV
    with open("registros.csv", mode="r", encoding="utf-8") as arquivo:

        # cria leitor CSV
        leitor = csv.reader(arquivo)

        # percorre linha por linha
        for linha in leitor:
            print(linha)


# Parte 4 - Criando planilha Excel
def salvar_excel():

    """
    Salva os registros em um arquivo Excel.
    """

    # cria a planilha
    wb = Workbook()

    # seleciona a aba ativa
    planilha = wb.active

    # renomeia a aba
    planilha.title = "Registros"


    # adiciona cabeçalho
    planilha.append(["ID", "Nome", "Email", "Idade", "Cidade", "Nota"])


    # busca os dados no banco
    dados = cursor.execute("SELECT * FROM registros").fetchall()


    # adiciona os dados linha por linha
    for linha in dados:
        planilha.append(list(linha))


    # salva a planilha
    wb.save("registros.xlsx")


    print("O arquivo registros.xlsx foi criado com sucesso!")


# Parte 5 - Criando arquivo XML
def salvar_xml():

    """
    Cria um arquivo XML contendo todos
    os registros armazenados no banco.
    """

    # cria a raiz do XML
    raiz = ET.Element("Registros")


    # busca os dados do banco
    dados = cursor.execute("SELECT * FROM registros").fetchall()


    # percorre os registros
    for linha in dados:

        # cria elemento Aluno
        aluno = ET.SubElement(raiz, "Aluno")


        # adiciona informações no XML
        ET.SubElement(aluno, "ID").text = str(linha[0])
        ET.SubElement(aluno, "Nome").text = linha[1]
        ET.SubElement(aluno, "Email").text = linha[2]
        ET.SubElement(aluno, "Idade").text = str(linha[3])
        ET.SubElement(aluno, "Endereco").text = linha[4]
        ET.SubElement(aluno, "Nota").text = str(linha[5])


    # cria a árvore XML
    arvore = ET.ElementTree(raiz)


    # salva o arquivo XML
    arvore.write("registros.xml", encoding="utf-8", xml_declaration=True)


    print("Arquivo 'registros.xml' criado com sucesso!")


# executa as funções
salvar_excel()
salvar_csv()
ler_csv()
salvar_xml()