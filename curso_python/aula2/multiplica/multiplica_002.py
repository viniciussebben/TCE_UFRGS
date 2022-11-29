"""
Programa soma
Requisito: Este programa pega dois números digitados pelo usuário, calcula o seu produto e coloca o resultado na tela com uma frase que explique o que é o resultado obtido.
Autor: Vinicius Ferreira Sebben
Data: 27/10/2022
Versão: 0.0.2
Correção do bug: chamar de parcela o que é, na verdade, fator.
"""


# Entrada
numero_1 = float(input("Digite o primeiro fator: "))
numero_2 = float(input("Digite o segundo fator: "))


# Processamento
produto = numero_1 * numero_2

# Saída
print(f"O produto dos números {numero_1} e {numero_2} é igual à {produto} .")
