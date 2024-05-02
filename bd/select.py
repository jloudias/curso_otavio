import sqlite3
from main import DB_FILE, TABLE_NAME
from tabulate import tabulate

#
# cria e conecta ao banco de dados
conn = sqlite3.connect(DB_FILE)  # conecta ao arquivo. Se não existir
cursor = conn.cursor()
#
# consulta a tabela
cursor.execute(f"SELECT * FROM {TABLE_NAME}")
#
# imprime os dados do cursor.
# OBS: o método fetchall() retorna uma tupla com os campos da linha
#
# Método 1 - Longo
# for row in cursor.fetchall():
#     _id = row[0]
#     name = row[1]
#     weight = row[2]
#     print(_id, name, weight)
#
# Método 2 - Desempacotamento
# for row in cursor.fetchall():
#     _id, name, weight = row
#     print(_id, name, weight)
#
# Método 3 - List comprehension e tabulate
my_data = [(row[0], row[1], row[2]) for row in cursor.fetchall()]
print(f"\nTabela {TABLE_NAME}\n")
print(tabulate(my_data, headers=["ID", "Name", "Weight"], tablefmt="orgtbl"))

# limpa os dados
cursor.close()
conn.close()
