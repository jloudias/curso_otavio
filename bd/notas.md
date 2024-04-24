# Banco de Dados
## Ambiente
- Python, sqlite3 e DBeaver Community
- criar conexão
- criar um cursor
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


## Referências
- [O que é cursor](https://www.youtube.com/watch?v=0ALGFmASo6I)
- [SQLite documentation](https://www.sqlite.org/doclist.html)
- [SQLite Tutorial](https://www.techonthenet.com/sqlite/index.php)
