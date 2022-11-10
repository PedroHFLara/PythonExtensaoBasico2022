#criação de funções

preco = 1999.90

#Calcular apenas 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcular_imposto()

def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

preco = 299
imposto = calcular_imposto(preco)
print(imposto)
print(f"Esse aqui é com a função (7%): {imposto}")


print(preco)
preco_produto = 100
print(preco_produto)

valores = [1.99, 24.50, 78.27, 1515.5]
for valor in valores:
  print(f"O imposto {valor} é {calcular_imposto(valor)}")
