# Banco de Dados
## Ambiente
- Python, sqlite3 e DBeaver Community
- O que é um cursor?
  - cursor é uma área de memória reservada para o armazenamento dos registros manipulados por comandos DML.
  - Exemplo: SELECT -> linhas retornadas vão para memória e podem ser acessadas pela aplicação
  - sempre que o comando DML manipular mais de uma linha de informação, dados irão para um cursor
  - tipos:
    - explícitos: 
      - aplicação necessita manipular cada um dos registros armazenados
      - aplicação declara o cursor
    - implícitos:
      - um comando manipula vários registros em uma única execução (UPDATE, DELETE)
      - banco de dados define, abre e fecha o cursor.

> LEMBRETE: Fechar as conexões e cursores ao sair da aplicação


## Primeiros Passos

### Sequência de Trabalho

- criar banco de dados
- criar e abrir conexão
- criar cursor
- executar operações com o cursor
- fazer commit na conexão
- fechar cursor e conexão

Exemplo:

```python 
import sqlite3
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()

cursor.close()
conn.close()
```

### Lembretes

> **IMPORTANTE:** Sempre que der, filtre e gerencie com SQL. 

- DELETE sem WHERE apaga todos registros
- Se mencionar ID em VALUES, atribuir valor NULL
- Reiniciar numeração dos ID
  
  `DELETE FROM sqlite_sequence WHERE name=”TABLE_NAME” `

- usar placeholders para evitar sql injection
  
  `INSERT INTO table(campo1, campo2) VALUES(?,?)`

- métodos de cursor: execute() e executemany()
- executemany pode conter listas, tuplas ou dicionários
  - dicionários -> nome da chave não precisa ser o nome do campo
  - use nomes das keys dos dicionários como placeholders
- métodos do cursor para SELECT
  - fetchall()
  - fetchmany()
  - 
- módulos para formatar saída de dados como tabela no terminal:
  - tabulate
  - PrettyTable
  - textable
  - termtables
  
## Referências
- [O que é cursor](https://www.youtube.com/watch?v=0ALGFmASo6I)
- [SQLite documentation](https://www.sqlite.org/doclist.html)
- [SQLite Tutorial](https://www.techonthenet.com/sqlite/index.php)
- [Printing lists as tabular data](https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data)
