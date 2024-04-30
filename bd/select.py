import sqlite3
from main import DB_FILE, TABLE_NAME
from tabulate import tabulate

#
# cria e conecta ao banco de dados
conn = sqlite3.connect(DB_FILE)  # conecta ao arquivo. Se não existir
cursor = conn.cursor()
#
# tabela
cursor.execute(f"SELECT * FROM {TABLE_NAME}")
# print("ID NAME        WEIGHT")
# print("=====================")
# for row in cursor.fetchall():
# fetchall() retorna uma tupla
# Método 1 - Longo
# _id = row[0]
# name = row[1]
# weight = row[2]
#
# Método 2 - Desempacotamento
# _id, name, weight = row

# print(_id, name, weight)
#
# Método 3 - List comprehension e tabulate
my_data = [(row[0], row[1], row[2]) for row in cursor.fetchall()]
print(tabulate(my_data, headers=["ID", "Name", "Weight"], tablefmt="orgtbl"))


cursor.close()
conn.close()
