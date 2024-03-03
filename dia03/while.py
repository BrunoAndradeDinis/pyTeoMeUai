# while
# %%

qtde = int(input("Quantos fodases você quer? "))
count = 1 

while count <= qtde: # enquanto ele for verdadeiro, ele vai continuar executando
    print("Fodase!")

    count += 1 #count = count + 1

# %%
while True:
    
    senha = input("Entre com a senha")

    if senha == "fodase": # aqui ele vai parar o while
      break

    elif senha == 'bruno':
       print("quase ...")
       continue
    
    print("Fodase")
    print("Outro fodase")
    print("Mais um fodase")

print("Saí! PORRA!")
# %%
# %%
# todos os números pares entre 1 - 15
contador = 1

while contador <= 15:
 
  if (contador % 2) == 0:
    print(contador)
  else:
    print("impar")
  contador += 1
# %%
