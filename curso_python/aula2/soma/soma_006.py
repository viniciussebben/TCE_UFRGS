"""
Programa soma
Requisito: Este programa pega dois números digitados pelo usuário e calcula a sua soma e coloca o resultado na tela com uma frase que explique o que é o resultado obtido.
Autor: Vinicius Ferreira Sebben
Data: 27/10/2022
Versão: 0.0.6
Alteração: possibilitar de o programa funcionar como módulo - validação de entrada
"""

# Definição de funções

def entrada():
    numero_1 = (input("Digite a primeira parcela: "))
    if isinstance(float(numero_1), float):
        numero_1 = float(numero_1)
    numero_2 = (input("Digite a segunda parcela: "))
    if isinstance(float(numero_2), float):
        numero_2 = float(numero_2)
    return [numero_1, numero_2]

def soma(x, y):
    return x + y

def saida(x, y, z):
    print(f"A soma dos números {x} e {y} é igual à {z} .")

def main():
    """Programa principal"""
    # Entrada
    lista_valores = entrada()

    # Processamento
    valor = soma(lista_valores[0], lista_valores[1])

    # Saída
    saida(lista_valores[0], lista_valores[1], valor)

# CHamada à execução da função principal
main() #está no escopo principal, olhar a tabulação)

# escopo global é o conjunto de variáveis definidas no programa principal
# escopo local é conjunto de variáveis definidas dentro das funções
# https://www.programiz.com/python-programming/methods/built-in/isinstance
# try/except/finally (criar exceções, no caso de testar o float para o caso do usuário digitar letra)

