"""
Programa calculadora basica
Requisitos: faça um programa de terminal que leia dois numeros digitados pelo usuario e a operação desejada entre adiçao, subtração, multiplicação e divisão e coleque o resultado na tela.
Autor: vinicius
Versão: 0.0.1
"""

# importação de módulos

import modelo
import view



# entrada

def entrada():
    """Esta função lê o teclado da calculadora."""
    i = 0
    dados = []
    while i < 2:
        dados.append(float(input("\n Digite o número {i+1}: ")))
        i += 1
    operacao = input("""\nDigite a operação desejada:
                    (+) para adição;
                    (-) para subtração;
                    (*) para multiplicação; e
                    (/) para divisão: """)
    dados.append(operacao)
    return dados
               

# processamento
"""
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x*y

def divisao(x, y):
    if y == 0:
        resultado = "Não existe divisão por zero"
    else:
        resultado = x / y
    return resultado
"""

"""
def saida(numero_1, numero_2, op, result):
    print(f"""O resultado da operação de {op} sobre os números {numero_1} e {numero_2} é igual a {result}.""")
def main():
    # entrada
    dados = entrada()
"""

def main():
    # entrada
    dados = view.entrada()

    # processamento
    if dados[2] == "+":
        resultado = modelo.adicao(dados[0], dados[1])
    elif dados[2] == "-":
        resultado = modelo.subtracao(dados[0], dados[1])
    elif dados[2] == "*":
        resultado = modelo.multiplicacao(dados[0], dados[1])
    elif dados[2] == "/":
        resultado = modelo.divisao(dados[0], dados[1])
    else:
        print("A operação não está definida.")
    


    # saida

    view.saida(dados[0], dados[1], dados[2], resultado)

if __name__ == "__main__":
    main()
    