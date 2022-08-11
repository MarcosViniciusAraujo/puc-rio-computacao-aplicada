'''
Author: @Marcos_Vinicius_Araujo

created_at: 10/08/2022
'''

def retorna_valor_quantidade_parcelas(valor_em_caixa: float, valor_do_presente: float) -> tuple:
    razao_presente_caixa = valor_do_presente / valor_em_caixa

    qto_e_quantidade_parcelas: tuple = None

    qto_parcelas = 0

    if razao_presente_caixa > 0.8:
        qto_parcelas = 5
        qto_e_quantidade_parcelas = (qto_parcelas, 1.1 * (valor_do_presente / qto_parcelas))
    elif razao_presente_caixa > 0.5:
        qto_parcelas = 3
        qto_e_quantidade_parcelas = (qto_parcelas, 1.08 * (valor_do_presente / qto_parcelas))
    else:
        qto_parcelas = 1
        qto_e_quantidade_parcelas = (qto_parcelas, 1.08 * (valor_do_presente / qto_parcelas))
    
    return qto_e_quantidade_parcelas


print(retorna_valor_quantidade_parcelas(100.0, 80))
print(retorna_valor_quantidade_parcelas(100.0, 60))
print(retorna_valor_quantidade_parcelas(100.0, 10))

