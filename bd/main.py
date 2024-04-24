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


cursor.close()
conn.close()
