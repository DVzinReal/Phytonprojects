# importa Flask para criar o website
from flask import Flask

# importa sqlite3 para acessar o banco de dados
import sqlite3 as sql



#cria a aplicação Flask
app = Flask(__name__)
# é o flask quem criar o servidor do site;
#abre a página no navegador;
#mostra os dados do banco em HTML


# conecta ao banco SQLite
conexao = sql.connect("registros.db", check_same_thread=False)

# cria cursor SQL
cursor = conexao.cursor()


# cria a rota principal do site
@app.route("/")
def pagina_inicial():

    # busca todos os registros do banco
    dados = cursor.execute("SELECT * FROM registros").fetchall()


    # cria o HTML da página
    html = """
    <html>

    <head>

        <title>Sistema de Registros</title>

        <style>

            body{
                font-family: Arial;
                background-color: #f4f4f4;
                padding: 20px;
            }

            h1{
                text-align: center;
            }

            table{
                width: 100%;
                border-collapse: collapse;
                background: white;
            }

            th, td{
                border: 1px solid black;
                padding: 10px;
                text-align: center;
            }

            th{
                background-color: #007BFF;
                color: white;
            }

        </style>

    </head>

    <body>

        <h1>Lista de Registros</h1>

        <table>

            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Email</th>
                <th>Idade</th>
                <th>Endereço</th>
                <th>Nota</th>
            </tr>
    """


    # percorre os registros
    for linha in dados:

        # adiciona cada linha na tabela HTML
        html += f"""
            <tr>
                <td>{linha[0]}</td>
                <td>{linha[1]}</td>
                <td>{linha[2]}</td>
                <td>{linha[3]}</td>
                <td>{linha[4]}</td>
                <td>{linha[5]}</td>
            </tr>
        """


    # finaliza o HTML
    html += """

        </table>

    </body>

    </html>
    """


    # retorna a página para o navegador
    return html


# inicia o servidor Flask
app.run(debug=True)