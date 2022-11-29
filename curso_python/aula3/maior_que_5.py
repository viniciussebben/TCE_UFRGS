"""
Programa: soma
Requisito: ler um número real digitado pelo usuário e colocar o resultado na tela.
Autor: Vinicius Ferreira Sebben
Data: 01/11/2022.
Versão: 0.0.1

"""
# Entrada

numero = float(input("\nDigite um número real: "))

# Processamento
if numero > 5:
    frase = f"O número {numero} é maior que 5."

# Saída

print(frase)

# nesse caso, o sistema só dará certo se o número digitado realmente for maior que 5
