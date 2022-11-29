"""
Programa divide
Requisito: Crie um programa que leia dois números do teclado, calcule a razão entre o primeiro e o segundo e escreva na tela o resultado.
Autor: Vinicius Ferreira Sebben
Data: 27/10/2022
Versão: 0.0.2
"""


# Entrada
# Explicar para o usuário o que o programa fará
print("Este programa calcula a razão de dois números dados pelo usuário do programa")
# \n para dar um espaço entre as linhas
numerador = float(input("\nDigite o numerador: "))
denominador = float(input("\nDigite o denominador: "))


# Processamento
# repetição = iteração
# decisão = seleção
razao = numerador / denominador

# Saída
print(f"\nA razão do numerador {numerador} pelo denominador {denominador} é igual à {razao} .")

# na aula, não finalizamos o erro ao tentar dividir numerador pelo denominador ZERO
