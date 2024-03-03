#Faça um programa que verifique se a pessoa pertence à família “calvo”.
# %%
nome = input("Entre com o seu nome completo")
nome = nome.lower()
print(nome.title())

if "calvo" in nome:
  print("Você tem Calvo no nome! \nVocê pertence a familia Calvo!")
else:
  print("Você não pertence a familia Calvo!")
# %%
