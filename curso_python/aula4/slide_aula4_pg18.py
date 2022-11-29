
lista = [1, 5, 2, 87, 31]
b = int(input("Digite o valor a procurar: "))
achou = False
x = 0
while x < len(lista):
    if lista[x] == b:
        achou = True
        break
    x+=1
if achou:
    print("%d achado na posição %d"%(b, x))
else:
    print("%d não encontrado"%b)
    
