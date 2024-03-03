# números 
# 1
# 10.0
# -1
# -10.0

# soma = 2 + 2 = 4 || vai retornar True

# Booleanos
True
False
# %%
idade = int

condicao = 20 > 18 # True or False


if condicao:
  print("Isso é verdade")

else:
  print("isso nunca vai acontecer")

# %%
  
# %%
idade = int(input("Entre com a sua idade:"))
cnh = input("Você tem CNH?")
cnh = cnh.lower()



if idade >= 18 and cnh == "sim": # só da continuidade se tudo estiver verdadeiro
  print("Siga em frente!")
else:
  print("BUSTED!")

condicao = idade >= 18 and cnh == "sim"
print(condicao)
# %%

#%%
print(True * 100) # 100 || True = 1
print(False * 100) # 0 || False = 0

# Tabela verdade E ||  só da true quando ambos forem true || quando for E/and/&
print("\nTabela verdade E\n")
print("True e True =", bool(1 * 1) )
print("True e False =", bool(1 * 0))
print("False e True =", bool(0 * 1)) 
print("False e False =", bool(0 * 0))

# Tabela verdade OU || vai da True sempre que tiver um True
print("\nTabela verdade OU\n")
print("True ou True =", bool(1 + 1))
print("True ou False =", bool(1 + 0))
print("False ou True =", bool(0 + 1)) 
print("False ou False =", bool(0 + 0))

# %%
