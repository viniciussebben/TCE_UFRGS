"""
Programa: soma
Requisito: ler um número real digitado pelo usuário e colocar o resultado na tela.
Autor: Vinicius Ferreira Sebben
Data: 01/11/2022.
Versão: 0.0.2
Alteração: inclusão da função else (caso contrário) para corrigir o problema caso digitasse número menor ou igual a 5.

"""
# Entrada

numero = float(input("\nDigite um número real: "))

# Processamento
# se tiver uma condição, isar if
# se tiver 2 condições, usar if e else
# se tiver mais de 2 condições, usar if, elif e else

if numero > 5:
    frase = f"O número {numero} é maior que 5."
elif numero == 5:
    frase = f"O número {numero} é igual a 5."
else:
    frase = f"O número {numero} é menor que 5."

    

# Saída

print(frase)

