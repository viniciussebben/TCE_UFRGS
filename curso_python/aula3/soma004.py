# na computação, repetição é chamada de iteração

"""
Programa: soma
Requisito (problema que o programa resolve): ler 4 números reais digitados pelo usuário, calcular a sua soma e colocar o resultado na tela.
Autor: Vinicius Ferreira Sebben
Data: 01/11/2022.
Versão: 0.0.4
Alteração: fazer o computador repetir a informação, sem eu precisar repetir os códigos.
"""

# Entrada e processamento de dados

# preciso d eum contador, pode ser a própria palavra ou a letra i
# função while (enquanto)
# o nome disso é LOOP
# o que endentar ou indentar, será repetido, para fazer isso, usar dois pontos

i = 0 # contador
soma = 0
while i<4:
    # posso usar o recurso print(i), que mostrará a cada linha o valor do i para o usuário
    numero = float(input("\nDigite a parcela: ")) # CTRL C interrompe a execução
    soma = soma + numero # acumulador
    i = i + 1 # laço de repetição ou loop de execução


# Saída


print(f"\nA soma dos números digitados é igual a {soma}")


