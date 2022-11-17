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
\tLocal: Rio de Janeiro\n\tData: 26/10/2022\n\tNome do foguete: Apolo 1026\n\tStatus: StatusRetired\n\
\tPreço: 100.0\n\tStatus da Missão: Success\n")
print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 2) Substitua os valores ausentes da coluna  Rocket por '0'. \n\
Como outra forma de tratamento, exclua as linhas onde o valor de Rocket é ausente. \n")
print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 3) Substitua 'Success' por 'Sucesso' e 'Failure' por 'Falha'.\n")
print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 4) Categorize as missões pelo preço.\n")
print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 5) Crie um filtro para encontrar os foguetes que custam mais que 100.0. \n\
Crie outro filtro para encontrar os foguetes que foram lançados antes do ano de 1970.\n\
Crie outro filtro para encontrar os foguetes que custam mais que 100.0 e que tenham resultado em um Sucesso.\n")
print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 6) Crie uma tabela de frequência sobre os valores absolutos na coluna Status Rocket. \n\
Além disso, crie uma tabela de frequência sobre os valores relativos na coluna Status Mission.\n")
print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 7) Faça um gráfico do tipo bar sobre a coluna Status Rocket. \n\
Faça outro gráfico de tipo pie sobre a coluna Status Mission. \n")
print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 8) a. Quanto foi gasto para a construção de todos os foguetes da base? \n\
\tb. Obtenha o custo médio dos foguetes através da coluna Rocket. \n\
\tc. Qual é o custo médio e a soma de todos os custos dos foguetes que resultaram em uma missão bem sucedida, por nome de companhia? \n")
print("\n-----------------------------------------------------")

print("\n-----------------------------------------------------")
print("\n 9) a. Faça um cruzamento simples da coluna Rocket com a coluna Status Rocket.  \n\
Faça outro cruzamento simples da coluna Rocket com a coluna Status Mission. \n\
\tb. Faça um cruzamento estruturado de colunas do dataset.\n")
print("\n-----------------------------------------------------")
