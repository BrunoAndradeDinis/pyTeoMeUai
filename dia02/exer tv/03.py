# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

# %%
tipo_sorvete = input("Entre com o tipo de sorvete: [casquinha/cestinha]")


sabor = input("Entre com o sabor do sorvete: [morango/creme/chocolate]")


cobertura = input("Entre com a cobertura que você quer: [caramelo/morango/chocolate]")

valor = 0

# tipo de sorvete
if tipo_sorvete == 'casquinha':
  valor += 2.5
elif tipo_sorvete == "cestinha":
  valor += 4.00
else:
  print("Sei édodp vao vor cagadp. escolha corretamente")

# tipo de cobertura
coberturas = 'caramelo,morango,chocolate'

if cobertura in cobertura:
  valor += 1.5
elif cobertura == '':
  pass
else:
  print('Seu pedido virá cagado, escolha corretamente')

print("Seu sorvete ", tipo_sorvete, "de", sabor," e cobertura de ", cobertura, " e custará: R$", round(valor, 2))
# qual o sabor

# %%

nome = "Brinu lindo"

print(nome in "Brinu ")

# %%
