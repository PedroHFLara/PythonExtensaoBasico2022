import aula4C

conexao, cursor = aula4C.conectar()

nome = input("Informe o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/vilão: ")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para Vilã(o): ")

sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"

cursor.execute(sql)
pessoa_id = cursor.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"
else: 
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cursor.execute(sql)
conexao.commit()
conexao.close()
