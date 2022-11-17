# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 08:52:37 2021

@author: Joisa
"""
# Consultando os slides e o código as series das aulas iniciais no arquivo 
# pd1_series_0001_ComFig.py prrencha o template abaixo
# OBS: no arquivo publicado com as series das aulas iniciais foi incluída 
# a visualização dos dados, com a exibição de gráficos a partir da 
# series srIdades na parte 2.


import pandas as pd
import matplotlib.pyplot as plt

srQtdMultas= pd.read_excel('carros20221.xlsx', usecols=(0,1), index_col=0, header=0,
                            squeeze= True)
srFab= pd.read_excel('carros20221.xlsx', usecols=(0,2), index_col=0, header=0,
                            squeeze= True)
print('\nQuantidade de Multas:')
print(srQtdMultas)
print('\nFabricantes:')
print(srFab)

print('---1---')
# Exiba os 5 veículos com maior quantidade de multas

print('---2---')
# Exiba a tabela de frequencia dos fabricantes


print('---3---')
# Exiba a menor quantidade de multa e um carro com a menor quantidade de 
# multas

print('---4---')
# Exiba a srFab ordenada alfabeticamente por fabricante


print('---5---')
# A partir da srQtdMultas crie a srCatQtMultas considerando 4 faixas de multas:
# de 0 até 4: POUCAS,
# de 5 até 15: FREQUENTES , 
# de 16 até 25: MUITAS, 
# acima de 25: ABSURDAS

print('---5A---')
# Exiba a srCatQtMultas

print('---5B---')
# Exiba tambem a tabela de frequencia das categorias de quantidades de multas

print('---5C---')
# Apresente o  grafico de pizza da tabela do item anterior

print('---6---')
#Qual o fabricante com o menor numero de veiculos?

print('---7---')
#Qual o total de multas no período considerado?

print('---8---')
#Exiba a relacao de fabricantes distintos

print('---9---')
#Quantos são os fabricantes distintos?

print('---10---')
#Grafico de barras da srMultas

print('---11---')
#Grafico de pizza da tabela de frequencia dos fabricantes

