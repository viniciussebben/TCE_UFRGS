lista = [1, 5, 2, 87, 31]
b = int(input("Digite o valor a procurar: "))
achou = False
for x in lista:
    if x == b:
        achou = True
        ind = lista.index(x)
        break
if achou:
    print(f"O valor {b} achado na posição {ind}.")
else:
    print(f"O valor {b} não foi achado.")
    
