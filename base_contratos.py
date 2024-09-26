import openpyxl
import models

path_base = "bases_de_dados/Base_Contratos.xlsx"

wb_obj = openpyxl.load_workbook(path_base)
planilha = wb_obj.active

todas_entradas = planilha.iter_rows(min_row=2, values_only=True)
contrato = models.BaseContratos

for entrada in todas_entradas:
    print(entrada)
    nova_entrada = contrato(
        idcontrato = entrada[0],
        idassinante = entrada[1],
        plano = entrada[2],
        forma_pagamento = entrada[3],
        duracao_plano = entrada[4],
        data_inicial = entrada[5],
        data_final = entrada[6]
    )   
    nova_entrada.save()
    
