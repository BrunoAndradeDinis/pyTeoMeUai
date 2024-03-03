# for
# %%

for i in "brinu lindu":

  if i == "b":
    continue # vai pular para a próxima iteração
  # elif i == " ":
  #   pass      || O pass não altera nada
  elif i == " ":
    continue
  print(i)
print(i)
# %%
# usando o range: range(15) || por padrão quando ele é declarado somente com o número máximo ele le como range(0,15), mas tem como você alterar o número inicial range(1,15) tcharam
seq = range(1,15)

for i in seq:
  if (i % 2) == 0:
    print(i)
# %%
qtde = int(input("Qual a quantidade de fodase você quer?"))

for i in range(qtde):
  print("Foda-se!")

# %%
