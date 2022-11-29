"""
Programa dobro
Requisitos: Este programa lê um numero digitado pelo usuario e imprime o seu dobro.
Autor: Vinicius
Versão: 0.0.2
Alteração: limpeza do documento (retirada dos #).
"""

# por ser procedural, precisa definir funções

## definição de funções

# entrada
def entrada():
    """Leitura do teclado do usuário."""
    numero = float(input("\nDigite um número: "))
    return numero

# processamento
def dobro(x):
    return 2*x

# saida

def saida(x, y):
    print(f"\nO dobro do número {x} é igual a {y}")
    
#Função principal

def main():
    valor = entrada()
    dobro_valor = dobro(valor)
    saida(valor, dobro_valor)

# execução da funçao principal

if __name__ == "__main__": # tem lógica criar essa linha para quando o programa tem mais de um arquivo
    main()

