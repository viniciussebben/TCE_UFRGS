# na computação, repetição é chamada de iteração

"""
Programa: soma
Requisito (problema que o programa resolve): ler um conjunto de números reais digitados pelo usuário, calcular a sua soma e colocar o resultado na tela.
Autor: Vinicius Ferreira Sebben
Data: 01/11/2022.
Versão: 0.0.5
Alteração: fazer o computador repetir a informação, sem eu precisar repetir os códigos.
"""

# Entrada e processamento de dados

# break interrompe a execução

soma = 0

while True:
    numero =  input("\nDigite a parcela ou pressione a tecla X para interromper: ")
    if numero == "X":
        break
    soma = soma + float(numero)
    


# Saída

print(f"\nA soma dos números digitados é igual a {soma} .")



