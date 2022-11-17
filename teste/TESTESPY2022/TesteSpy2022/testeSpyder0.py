# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:06:08 2021

@author: Joisa

Voce obrigatoriamente deve instalar o  (spyder) como  informado 
nos slides de apresentacao do curso publicado no tópico no EAD

Esse programa deve ser executado para verificar se o spyder esta´
corretamente instalado.

Esse arquivo (testeSpyder0.py) e o arquivo de dados notas2022.xlsx 
devem estar na mesma pasta.

Caso tenha problemas busque as monitorias de apoio.

Nao sera possivel prosseguir no bloco2 do curso sem a correta instalacao do 
spyder

"""

import pandas as pd
import matplotlib.pyplot as plt


#---------------------------------------------------------------
#---------------------------------------------------------------
#                      
# Trabalhando com um DataFrames criado a partir de um arquivo excel:
# arquivo notas2022.xlsx: com as notas dos alunos 
# O arquivo deve estar na mesma pasta que o .py
# Coluna 0 servira de indice (index_col=0)
# O arquivo tem linha de cabecalho (header=0)

dfAl = pd.read_excel('notas2022.xlsx', index_col=0, header=0)
print('\n dfAl')
print(dfAl.columns)

print('\n Tab Freq Curso:')
print(dfAl.CURSO.value_counts())

print('\n Media das provas')
print(dfAl[['P1','P2']].mean())

dfAl.CURSO.value_counts().plot.pie(autopct='%.1f')
plt.show()

nome=input('Entre seu nome:')
print('Aluno %s executou o programa'%nome)

