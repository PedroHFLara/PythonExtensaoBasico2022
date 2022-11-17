#Importar
import sqlite3

#Função conectar()
def conectar():

  #Estabelecer conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")

  #Criar objeto do tipo cursos
  cursor = conexao.cursor()

  return conexao, cursor
  