#Importar biblioteca
import sqlite3

#estabelecer conexão com bancos de dados
conexao = sqlite3.connect("dc_universe.db")

#criar um ojeto de tipo cursor
cursor = conexao.cursor()

#comando para inserir um personagem
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry', 'Herói(na)')"

#Executar o comando SQL
cursor.execute(sql)

#Confirmar INSERT com commit() e fechar o banco
conexao.commit()
conexao.close()
