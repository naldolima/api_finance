import sqlite3

connection = sqlite3.connect("./preco.db")

# Criação do cursor, elemento que "aponta" para os dados e permite percorrê-los
cursor = connection.cursor()

# Definição da string de busca no banco de dados
query = "SELECT * FROM preco"

# Execução da consulta pelo cursor
cursor.execute(query)

# Extração dos resultados
result = cursor.fetchall()

connection.close()


for row in result:
    print(row)