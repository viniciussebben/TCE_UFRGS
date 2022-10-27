"""
Programa soma_aula-26-10-2022
Requisito: Este programa pega dois números inteiros, digitados pelo usuário, calcula a soma dele e coloca o resultado na tela, com a explicação do que se refere o resultado obtido.
Autor: Vinicius Ferreira Sebben
Data: 27/10/2022
Versão: 0.0.2
Correção: Segunda versão, para corrigir o texto explicativo do programa par ao usuário, incluindo a palavra "inteiros" após "números"
"""


# Entrada
# Explicar para o usuário o que o programa fará
print("Este programa calcula a soma de dois números inteiros dados pelo usuário do programa")
# \n para dar um espaço entre as linhas
numero_1 = int(input("\nSenhor usurário, digite o primeiro número inteiro: "))
numero_2 = int(input("\nSenhor usuário, digite o segundo número inteiro: "))


# Processamento
soma = numero_1 + numero_2

# Saída
print(f"\nA soma dos números inteiros {numero_1} e {numero_2} é igual à {soma} .")
