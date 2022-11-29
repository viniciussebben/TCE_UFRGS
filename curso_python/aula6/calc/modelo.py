""" Módulo modelo.py
Requisito: Este módulo agrega as funções que modelam as operações realizadas pela calculadora.
Autor: Vinicius
Data: 16/11/2022
Versão 0.0.1
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