import openpyxl
import models

path_base = "bases_de_dados/Base_Assinantes.xlsx"

wb_obj = openpyxl.load_workbook(path_base)
planilha = wb_obj.active

todas_entradas = planilha.iter_rows(min_row=2, values_only=True)
for entrada in todas_entradas:
    nova_entrada = models.BaseAssinantes(
        idassinante = entrada[0],
        sexo = entrada[1],
        data_nascimento = entrada[2],
        estado_civil = entrada[3],
        escolaridade = entrada[4],
        cidade = entrada[5],
        uf = entrada[6]
    )
    nova_entrada.save()
    
