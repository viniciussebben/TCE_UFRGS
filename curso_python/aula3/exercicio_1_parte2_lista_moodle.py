"""
Nome: exercício 1 da lista - estrutura de controle seleção
Requisitos:  leia um número e imprima na tela o seu dobro se ele for menor do que 10. Se o número
for de 10 até 20, imprima a sua metade. Em qualquer outro caso, imprima na tela que o
número n˜ao ´e v´alido.
Autor: Vinicius Ferreira Sebben
Data: 01/11/2022
Versão: 0.0.1
"""

# entrada

numero = float(input("Digite um número: "))


# processamento

resultado = 0

if numero < 10:
    resultado = 2*numero

elif numero >= 10 and numero <= 20:
    resultado = numero/2

else:
    resultado = "O número não é válido."


# saída

print(resultado)
