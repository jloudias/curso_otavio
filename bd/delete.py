import sqlite3
from main import DB_FILE, TABLE_NAME
from tabulate import tabulate

#
# cria e conecta ao banco de dados
conn = sqlite3.connect(DB_FILE)  # conecta ao arquivo. Se não existir
cursor = conn.cursor()
#
# consulta a tabela em busca do nome do usuário
username = input("Digite o nome do usário:\n").lower()
cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE name LIKE '%{username}%'")
#
# imprime os dados do cursor.
# OBS: o método fetchall() retorna uma tupla com os campos da linha
my_data = [(row[0], row[1], row[2]) for row in cursor.fetchall()]
print(f"\nTabela {TABLE_NAME}\n")
print(tabulate(my_data, headers=["ID", "Name", "Weight"], tablefmt="orgtbl"))

# DELETE 1 - exclusão de todos usuários encontrados
# resp = input("Tem certeza que deseja exluir esses registros?(S/N): ").lower()
# if resp == "s":
#     cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE name LIKE '%{username}%'")
#     conn.commit()
#
# DELETE 2 - exclui usuário por ID
userid = int(input("Digite o ID do usuário a ser excluído: "))
cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = {userid}")
conn.commit()
#
# exibe dados após exclusão
cursor.execute(f"SELECT * FROM {TABLE_NAME}")
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

# limpa os dados
cursor.close()
conn.close()
