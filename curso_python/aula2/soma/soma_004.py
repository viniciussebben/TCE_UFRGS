"""
Programa soma
Requisito: Este programa pega dois números digitados pelo usuário e calcula a sua soma e coloca o resultado na tela com uma frase que explique o que é o resultado obtido.
Autor: Vinicius Ferreira Sebben
Data: 27/10/2022
Versão: 0.0.4
Alteração: criação da função soma.
"""

def soma(x, y):
    return x + y

# Entrada
numero_1 = float(input("Digite a primeira parcela: "))
numero_2 = float(input("Digite a segunda parcela: "))


# Processamento
valor = soma(numero_1, numero_2)


# Saída
print(f"A soma dos números {numero_1} e {numero_2} é igual à {valor} .")
