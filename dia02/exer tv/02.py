# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50
# %%
escolha = input("Você gostaria de um garrafa de água mineral ou com gás? [mineral/gas]")
escolha = escolha.lower()
quantidade = int(input("quantas águas você deseja?"))

total = 0

if escolha == "mineral":
  total = 1.5 * quantidade
elif escolha == "gas":
  total = 2.5 * quantidade
else:
  print("Faça uma escolha válida!")

print("Você tem que pagar R$", round(total,2))
# %%