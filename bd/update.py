import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()


def show_data():
    sql1 = f"SELECT * FROM {TABLE_NAME}"
    cursor.execute(sql1)
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)


show_data()

user_id = int(input("Digite o ID do usuário a ser alterado: "))
new_name = input("Digite o novo nome do usuário: ")

sql2 = f"UPDATE {TABLE_NAME} SET name='{new_name}' WHERE id={user_id}"
cursor.execute(sql2)
conn.commit()

show_data()

cursor.close()
conn.close()
