"""
Programa dobro
Requisitos: Este programa lê um numero digitado pelo usuario e imprime o seu dobro.
Autor: Vinicius
Versão: 0.0.1
"""

# por ser procedural, precisa definir funções

## definição de funções

# entrada
def entrada():
    """Leitura do teclado do usuário."""
    numero = float(input("\nDigite um número: ")) # depois disso, ele apaga o numero da memoria, precisa retornar
    return numero # precisa pegar na função principal

"""
def converte_numero(texto):
    numero = float(texto)
    return numero
    se quisesse ser mais purista, por a função entrada deveria apenas entrar dado e nao processar anda
    """

# processamento
def dobro(x):
    # pass ## para o interpretador passar e não dar bug
    return 2*x


# saida

def saida(x, y):
    print(f"\nO dobro do número {x} é igual a {y}")

    
#Função principal

def main():
    # entrada de dados
    valor = entrada()
    # print (valor) - foi um teste apenas
    
    #cálculo do dobro do valor digitado pelo usuario
    dobro_valor = dobro(valor)
    # print(dobro_valor)

    # saida de dados
    saida(valor, dobro_valor)



# execução da funçao principal

main()
