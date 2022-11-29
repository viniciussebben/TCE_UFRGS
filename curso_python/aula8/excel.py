"""
Projeto: criar planilha Excel com colunas de contas, receitas, despesas e resultados.
Autor: Vinicius Ferreira Sebben
Data: 29/11/2022
Versão: 0.0.1
"""


from openpyxl import Workbook
orcamento = Workbook()

Novembro = orcamento.active

Novembro['A1'] = "Contas"

Novembro["B1"] = "Receitas"

Novembro["C1"] = "Despesas"

Novembro["D1"] = "Resultados"

Novembro["A2"] = "alimentação"
Novembro["A3"] = "energia"
Novembro["A4"] = "transporte"

# entrada
# Novembro["A2"] = valores[0]
Novembro["B2"] = 1000
Novembro["C2"] = 200
Novembro["C3"] = 200
Novembro["C4"] = 200

# processamento
Novembro["D2"] = Novembro["B2"].value - (Novembro["C2"].value + Novembro["C3"].value + Novembro["C4"].value)

# saída
Novembro["D2"].value


Novembro["A1"].value

# salvar
orcamento.save("orcamento.xlsx")
