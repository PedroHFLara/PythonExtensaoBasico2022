# NOTA

nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota de 0 a 10: "))

if(nota == 10):
  print(f"{nome}, Aprovado.")
elif(nota >= 6 and nota < 10):
  print(f"{nome}, Recuperação.")
else:
  print(f"{nome}, Reprovado.")
  