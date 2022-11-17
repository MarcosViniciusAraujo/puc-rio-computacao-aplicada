#############################################################################################################
#                                                                                                           #            
#                                                Turma: 33C                                                 #   
#                                                                                                           #  
#        Professora: Joisa                                                                                  #
#        Integrante 1: Felipe Frighetto Gonzalez - 1910438                                                  #
#        Integrante 2: Marcos Vinicius Araujo de Almeida - 1910869                                          #
#                                                                                                           #            
#                                                                                                           #            
#############################################################################################################



import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

raw = pd.read_excel('Space.xlsx', header=0, usecols=(2, 3, 4, 5, 6, 7, 8)).squeeze("columns")

raw['Datum'] = pd.to_datetime(raw['Datum'], dayfirst=True)


print("\n-----------------------------------------------------")
print("\n 1) Adicione na base de dados um novo registro com as novas informações:\n\tNome da Companhia: SpaceXRJ\n\
\tLocal: Rio de Janeiro\n\tData: 16/11/2022\n\tNome do foguete: Apollo 1026\n\tStatus: StatusRetired\n\
\tPreço: 100.0\n\tStatus da Missão: Success\n")

to_add = {
    "Company Name":"SpaceXRJ",
    "Location":"Rio de Janeiro",
    "Datum":datetime(2022, 11, 16),
    "Detail":"Apollo 1026",
    "Status Rocket": "StatusRetired",
    "Rocket": 100.0,
    "Status Mission": "Success"
}

raw = raw.append(to_add, ignore_index=True)


print(raw.loc[raw['Datum'] == '16/11/2022'])


print("\n-----------------------------------------------------")


print("\n-----------------------------------------------------")
print("\n 2) Substitua os valores ausentes da coluna  Rocket por '0'. \n\
Como outra forma de tratamento, exclua as linhas onde o valor de Rocket é ausente. \n")

raw['Rocket'] = raw['Rocket'].fillna(0)
raw['Location'] = raw['Location'].fillna('Location Unknown')


print(raw.head())


print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 3) Substitua 'Success' por 'Sucesso' e 'Failure' por 'Falha'.\n")

raw_renomeado = raw["Status Mission"].replace({"Success": "Sucesso", "Failure": "Falha"})

print(raw_renomeado.head())

print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 4) Categorize as missões pelo preço.\n")
print("\n-----------------------------------------------------")

raw_cutted = pd.cut(raw['Rocket'], bins=[0, 50, 75, raw['Rocket'].max()], labels=['Baixo', 'Mediano', 'Caro'], include_lowest=True)


print(raw_cutted)


print("\n-----------------------------------------------------")
print("\n 5) Crie um filtro para encontrar os foguetes que custam mais que 100.0. \n\
Crie outro filtro para encontrar os foguetes que foram lançados antes do ano de 1970.\n\
Crie outro filtro para encontrar os foguetes que custam mais que 100.0 e que tenham resultado em um Sucesso.\n")

f1 = raw['Rocket'] > 100
f2 = raw['Datum'] < datetime(1970, 1, 1)
f3 =  raw['Status Mission'] == 'Success'
fc = f1 & f3


print(raw.loc[f1].head())
print(raw.loc[f2].head())
print(raw.loc[f3].head())
print(raw.loc[fc].head())


print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 6) Crie uma tabela de frequência sobre os valores absolutos na coluna Status Rocket. \n\
Além disso, crie uma tabela de frequência sobre os valores relativos na coluna Status Mission.\n")


freq_rocket = raw['Status Rocket'].value_counts()

print(freq_rocket)


freq_mission = raw['Status Mission'].value_counts(normalize=True) * 100

print(freq_mission)


print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 7) Faça um gráfico do tipo bar sobre a coluna Status Rocket. \n\
Faça outro gráfico de tipo pie sobre a coluna Status Mission. \n")

freq_rocket.plot(kind='bar', title='Status Rocket')

plt.show()

freq_mission.plot(kind='pie', title='Status Mission')

plt.show()



print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 8) a. Quanto foi gasto para a construção de todos os foguetes da base? \n\
\tb. Obtenha o custo médio dos foguetes através da coluna Rocket. \n\
\tc. Qual é o custo médio e a soma de todos os custos dos foguetes que resultaram em uma missão bem sucedida, por nome de companhia? \n")

print(f"Gasto total: {raw['Rocket'].sum()}")
print(f"Gasto médio: {raw['Rocket'].mean()}")


filtro = raw['Status Mission'] == 'Success'

df1 = raw[filtro].groupby('Company Name').sum().rename({'Rocket': "Soma"})
df2 = raw[filtro].groupby('Company Name').mean().rename({'Rocket': "Media"})

result = pd.concat([df1, df2], axis=1)

print(result)
print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 9) a. Faça um cruzamento simples da coluna Rocket com a coluna Status Rocket.  \n\
Faça outro cruzamento simples da coluna Rocket com a coluna Status Mission. \n\
\tb. Faça um cruzamento estruturado de colunas do dataset.\n")


cross1 = pd.crosstab(index=raw['Status Rocket'], columns=raw['Rocket'])
cross2 = pd.crosstab(index=raw['Status Mission'], columns=raw['Rocket'])

print(cross1)
print(cross2)

cross3 = pd.crosstab(raw.index, [raw['Status Mission'], raw['Status Rocket']], normalize=True)

print(cross3)

print("\n-----------------------------------------------------")
