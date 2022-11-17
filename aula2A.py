# comando input(): quero permitir que o usuário digite algo...
nome = input("Digite seu nome: ")

idade = int(input("Qual a sua idade? "))

#comando de saída / exibir na tela
print(f"Boa noite, seu nome é {nome}")

print(f"Sua idade é: {idade}")
          
dobro = idade * 2

print("O dobro da idade informada é {}".format(dobro))

if idade >= 18:
  print("Você é maior de idade, que beleza! Já pode dirigir.")
else:
  print("Você é jovem ainda.")

genero = input("Informe o genero M=Masculino ou F=Feminino : ")
if idade >= 18 and genero == "M":
  print("Você prestou ou vai prestar o serviço militar obrigatário.")
else:
  print("Você não precisa prestar serviço militar obrigatório.")
