"""Programa calculadora_basica
Requisitos: Fazer um programa de calculadora com operações básicas, que leia dois números
digitados pelo usuário e a operação desejada entre as seguintes: adição,
subtração, multiplicação e divisão, e coloque o resultado na tela.
Autor: Vinicius Ferreira Sebben
Data: 29/11/2022
Versão: 0.0.3
"""
"""
Enfreitei muita dificuldade em conseguir entender a linguagem e as funções, precisei acompanhar a aula e o modelo do professor.
"""

# Entrada

def entrada():
    i = 0
    dados = []
    while i < 2: # primeiro número é o "zero" e segundo é o "um", menor que 2 para deixar o usurário digitar apenas 2
        dados.append(float(input("\n Digite o número {i+1}: "))) # float para que o python entenda ser número
        i += 1
    operacao = input("""\nDigite a operação desejada:
                     (+) para adição;
                     (-) para subtração;
                     (*) para multiplicação, e
                     (/) para divisão: """)
    dados.append(operacao)
    return dados


# Processamento

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x*y

def divisao(x, y):
    if y == 0: # lembrar que nessa operação não existe divisão por zero
        resultado = "Não existe divisão por zero"
    else:
        resultado  = x / y
    return resultado

def saida(numero1, numero2, operacao, resultado):
    print(f"""O resultado da operação de {operacao} sobre
os números {numero1} e {numero2} é igual a {resultado}.""")

def main():
    # entrada
    dados = entrada()

    # processamento
    if dados[2] == "+":
        resultado = adicao(dados[0], dados[1])
    elif dados[2] == "-":
        resultado = subtracao(dados[0], dados[1])
    elif dados[2] == "*":
        resultado = multiplicacao(dados[0], dados[1])
    elif dados[2] == "/":
        resultado = divisao(dados[0], dados[1])
    else:
        print("A operação não está definida.")

    # saida
    saida(dados[0], dados[1], dados[2], resultado)

if __name__ == "__main__":
    main()
