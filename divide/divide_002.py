"""
Programa divide
Requisito: Crie um programa que leia dois números inteiros do teclado, calcule a razão entre o primeiro e o segundo e escreva na tela o resultado.
Autor: Vinicius Ferreira Sebben
Data: 27/10/2022
Versão: 0.0.2
Correção: incluir informação "int" após "print" na saída de dados.
"""


# Entrada
# Explicar para o usuário o que o programa fará
print("Este programa calcula a razão de dois números inteiros dados pelo usuário do programa")
# \n para dar um espaço entre as linhas
numerador = int(input("\nDigite o numerador: "))
denominador = int(input("\nDigite o denominador: "))


# Processamento
razao = numerador / denominador

# Saída
print(int(f"\nA razão do numerador {numerador} pelo denominador {denominador} é igual à {razao} ."))
