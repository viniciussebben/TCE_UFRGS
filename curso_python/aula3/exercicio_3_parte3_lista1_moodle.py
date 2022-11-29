"""
Nome: exercício 3 parte 3 lista 1 moodle
Requisitos: leia cinco n´umeros e imprima na tela o quadrado de cada um deles.
Autor: Vinicius Ferreira Sebben
Data: 01/11/2022
Versão: 0.0.1
"""


# entrada, processamento e saída

i = 0

while i < 5:
    numero = float(input("\nDigite um número: ")) # entrada
    print (f"\nO quadrado do número digitado é igual a {numero**2}") # processamento e saída de dados
    i += 1 # i = i + 1


