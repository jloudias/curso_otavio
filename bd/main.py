import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent  # root da aplicação
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME  # path do arquivo de dados do sqlite3
TABLE_NAME = "customers"
#
# cria e conecta ao banco de dados
conn = sqlite3.connect(DB_FILE)  # conecta ao arquivo. Se não existir
cursor = conn.cursor()
#
# cria tabela
sql = f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
sql += "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
sql += "name TEXT, weight REAL)"

cursor.execute(sql)
conn.commit()  # comita o bd
#
# CUIDADO: fazendo delete sem where
cursor.execute(f"DELETE FROM {TABLE_NAME}")
#
# zerar sequencia de ID
cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{TABLE_NAME}'")
#
# CUIDADO: sql injection
# inserindo dados
sql2 = """
    INSERT INTO customers(id, name, weight)
    VALUES
    (NULL, 'Jorge Dias', 79.9), 
    (NULL, 'Jussara Belem', 70.2),
    (NULL, 'Sátia Dias', 55.5),
    (NULL, 'Laura Tamayo', 15.5)
"""
cursor.execute(sql2)
#
# usando placeholders e listas de tuplas
sql3 = f"INSERT INTO {TABLE_NAME}(name, weight) VALUES (?,?)"
cursor.execute(sql3, ["Sinthia Chata", "33.4"])
#
# executemany
cursor.executemany(
    sql3, [("Pedro", 22.2), ("Maria das Graças", 33.4), ("Pedro Calmon", 33.5)]
)
#
# usando placeholders e dicionários
sql4 = f"INSERT INTO {TABLE_NAME}(name, weight) VALUES(:dn, :dw)"
cursor.executemany(
    sql4, [{"dn": "Marcos Cintra", "dw": 22.2}, {"dn": "Pedro da Zefa", "dw": 11.1}]
)

conn.commit()

cursor.close()
conn.close()
