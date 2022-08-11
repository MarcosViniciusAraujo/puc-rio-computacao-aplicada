'''
Author: @Marcos_Vinicius_Araujo

created_at: 10/08/2022
'''

def trataUmLaboratorio(file):
    
    dados = []

    for i in range(8):
        linha = file.readline()
        infos = linha.strip().split(';')

        lab = infos[0]
        hora = int(infos[1])
        temperatura = float(infos[2])
        grau = int(infos[3])

        if dados == []:
            dados = [lab, [hora, temperatura], [hora, grau]]
            continue
        
        if dados[1][1] > temperatura:
            dados[1] = [hora , temperatura]

        if dados[2][1] > grau:
            dados[2] = [hora, grau]
    
    return (dados[0], (dados[1][0], dados[1][1]), (dados[2][0], dados[2][1]))


with open('RegistrosLab.txt', 'r') as f:
    for i in range(6):
        print(trataUmLaboratorio(f))

    
