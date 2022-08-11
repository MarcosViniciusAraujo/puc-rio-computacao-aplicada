'''
Author: @Marcos_Vinicius_Araujo

created_at: 10/08/2022
'''


def um_sensor():
    
    # Le o arquivo
    with open('Registros.txt', 'r') as f:

        contagem = dict()

        for line in f:

            infos = line.strip().split(';')

            sensor = infos[0]
            hora = int(infos[1])
            temperatura = float(infos[2])
            grau = float(infos[3])

            # Reescreve a contagem
            if contagem.get(sensor) == None:
                contagem[sensor] = {
                    "temperatura": [hora, temperatura],
                    "grau": [hora, grau]
                }
                continue
            
            # checa se a temperatura é menor
            if contagem[sensor]['temperatura'][1] > temperatura:
                contagem[sensor]['temperatura'] = [hora, temperatura]
            
            #checa se o grau é menor
            if contagem[sensor]['grau'][1] > grau:
                contagem[sensor]['grau'] = [hora, grau]

    # Exibe os valores
    for key, value in contagem.items():
        print(f"Sensor {key}- Temperatura Mínima {value['temperatura'][1]}ºC às {value['temperatura'][0]}h e Umidade Mínima: {value['grau'][1]}% às {value['grau'][0]}h")


um_sensor()