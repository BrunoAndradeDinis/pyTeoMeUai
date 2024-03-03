# Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

# %%

nome = input("Entre com o seu nome completo")
nome = nome.lower()
print(nome.title())

if "calvo" in nome:
  print("Você tem Calvo no nome! \nVocê pertence a familia Calvo!")

elif "silva" in nome:
  print("Você tem Silva no nome! \nVocê pertence a familia Silva!")
else:
  print("Você não pertence a familia Calvo e nem a familia Silva!")
# %%
