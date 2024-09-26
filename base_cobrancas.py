import openpyxl
import models

path_base = "bases_de_dados/Base_Cobranças.xlsx"

wb_obj = openpyxl.load_workbook(path_base)
planilha = wb_obj.active

todas_entradas = planilha.iter_rows(min_row=2, values_only=True)
cobranca = models.BaseCobrancas

for entrada in todas_entradas:
    print(entrada)
    nova_entrada = cobranca(
        idcobranca = entrada[0],
        idcontrato = entrada[1],
        status = entrada[2],
        data_vencimento = entrada[3],
        data_pagamento = entrada[4],
        data_cancelamento = entrada[5],
        valor_cobranca = entrada[6]
    )   
    nova_entrada.save()
    
