# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:06:08 2021

@author: Joisa

Series: Introducao
Exemplos e exercicios basicos
Criacao, indices e valores, tamanho, acesso, exibicao,
inclusao, alteracao, 
Eliminacao de elementos : drop()/dropna() ,
Ordenacao 
    por valor: sort_values()
    por indices: sort_index()
Copia: copy()
    
OBS: os metodos drop(), dropna(), sort_values(), sort_index() 
retornam uma COPIA da series, sem alteracao da series original.
Para alterar a series original, deve-se usar dentro da chamada 
desses metodos o parametro (inplace= True) 


Voce deve preencher o codigo a seguir para obter o resultado 
desejado

"""
# NOME:
# TURMA:
# MAT:
# PROF: 
# Exercicio sobre series (introducao) nao pontuado



import pandas as pd

#NOVO => para as figuras
import matplotlib.pyplot as plt

'''
Criando uma series a partir de duas listas:
uma para valores e outra para indices
'''


lpessoas= ['tita','ludo','yuki','zeus','matt','deby','dave','babi', 'lulu']
lprof= ['medico','professor','advogado','filosofo','professor','medico','dentista','professor', 'fisioterapeuta']
lidades= [45,30,67,37,26,58,43,38,29]


'''
#---------------------------------------------------------------
#---------------------------------------------------------------
#                    PARTE 1
srProfissoes= pd.Series(lprof,index = lpessoas)
print('\n Series:')
print(srProfissoes)


# Exiba o indice =>  .index
print('\n Indice:')
print(srProfissoes.index)


# Exiba os valores =>  .values
print('\n Valores:')
print(srProfissoes.values)


# Exiba numero de elementos (tamanho) =>  .size
print('\n Tamanho:')
print(srProfissoes.size)


# Profissao de um individuo => .loc[indice]
print('\n Profissao do matt:')
print(srProfissoes.loc['matt'])

print('\nLista so com o matt')
print(srProfissoes.loc[['matt']])

print('prof do segundo,terc, quarto')
print(srProfissoes.iloc[1:4])



# Profissoes de varios individuos => .loc[[lista de indices]]
print('\n Profissoes do yuki, deby e babi :')
print(srProfissoes.loc[['yuki','deby', 'babi']])


# Profissoes dos 3 primeiros da series => .head()
print('\n Profissoes dos 3 primeiros:')
print(srProfissoes.head(3))


# Profissoes dos 6 ultimos da series => .tail()
print('\n Profissoes dos 6 ultimos:')
print(srProfissoes.tail(6))


# Alterar a profissao da lulu para 'chef' => .loc[] = ...
# Exibir a profissao da lulu antes e depois da alteracao
print('\n Alterando lulu')
srProfissoes.loc['lulu']= 'chef'
print(srProfissoes)

#Incluir um novo elemento: ruan, medico => .loc[] = ...
#Exibir a series depois da inclusao, assim como o seu tamanho
print('\n Incluindo ruan')
srProfissoes.loc['ruan']= 'medico'
print(srProfissoes)

#Apenas exibir a series SEM  yuki, dave => .drop([lista de indices])
print('\n Sem yuki, dave')
print(srProfissoes.drop(['yuki', 'dave']))


#Exibir a series srProfissoes 
print('\n Series:')
print(srProfissoes)


#Eliminar da srProfissoes yuki e lulu => .drop([lista de indices], inplace=True)
srProfissoes.drop(['yuki', 'lulu'], inplace=True)

#Exibir a series srProfissoes atualizada  e o tamanho
print('\n Series atualizada:')
print(srProfissoes)

#Apenas exibir a series  srProfissoes ordenada por profissao (valores) => .sort_values()
print('\n Exibicao da Series ordenada por profissao:')
print(srProfissoes.sort_values())

#Ordenar a series pelo nome das pessoas => .sort_index(inplace=True)
#Depois exibir a series alterada
print('\n Series srProfissoes alterada (ordenada por indice) :' )
srProfissoes.sort_index(inplace=True)
print(srProfissoes)

###########################################
# COMPLEMENTO
print('\nQuais são as profissões (distintas)')
print(srProfissoes.unique())

print('\nQuantas são as profissões (distintas)')
print(srProfissoes.nunique())


print('\nTabela de frequencia das profissoes')
srTabFreqProf=srProfissoes.value_counts()
print(srTabFreqProf)

print('Tab freq Percentual (RELATIVA)')
srTabFrPerc1= srTabFreqProf/srProfissoes.size *100
print(srTabFrPerc1)
print('\n')
srTabFrPerc2= srProfissoes.value_counts(normalize=True)*100
print(srTabFrPerc2)


print('\nIN')
print(srProfissoes.index.values)

'''


'''

#---------------------------------------------------------------
#---------------------------------------------------------------
#                        PARTE 2
# A partir das listas lpessoas e lidades crie a series srIdades 
# em os valores devem ser as idades e os indices os nomes das pessoas

srIdades = pd.Series(lidades, index=lpessoas )
#Exiba devidamente identificados:
# a series
# os indices
# os valores
print('\n----- srIdades -----')
print('\n Series srIdades:')
print(srIdades)
print('\n Indice (srIdades):')
print(srIdades.index)
print('\n Valores (srIdades):')
print(srIdades.values)
# Exiba numero de elementos (tamanho) =>  .size
print('\n Tamanho:')
print(srIdades.size)

# a idade da tita
# os 3 ultimos elementos
# os 7 primeiros elementos da series, ordenados pela idade (nao alterar a series)
# os 3 primeiros mais novos
# a series original sem a babi (nao alterar)

print('\n Idade da tita')
print(srIdades.loc['tita'])

print('\n 3 ultimos')
print(srIdades.tail(3))

print('\n7 primeiros ordenados pela idade')
print(srIdades.head(7).sort_values())


print('\n3 primeiros mais novos')
print(srIdades.sort_values().head(3))


print('\nExibir sem a babi')
print(srIdades.drop('babi'))


###########################################
# COMPLEMENTO
#  Series com valores numéricos => há medidas de interesse
print('\nQual a idade máxima?')
print(srIdades.max())

print('\nQual a idade mínima?')
print(srIdades.min())

print('\nQual média das idades?')
print(srIdades.mean())

print('\nQual a mediana das idades?')
print(srIdades.median())

print('\nIdade minima:',srIdades.min() )
print('\nUm indivíduo com a idade minima?',srIdades.idxmin() )
print('\nIdade maxima:',srIdades.max())
print('\nUm indivíduo com a idade maxima?',srIdades.idxmax() )

print('\nTabela de Frequencia das idades') # Nao fica interessante
print(srIdades.value_counts())

#################################################
# Criando categorias de idades => método pd.cut()
print('\nCriando 3 categorias')
srCat1= pd.cut(srIdades, bins=3 )
print(srCat1)

print('\nCriando 3 categorias com extremos definidos')
srCat2= pd.cut(srIdades, bins=[0,30,55,srIdades.max()])
print(srCat2)

print('\nQuantos indivíduos em cada categoria?')
print(srCat2.value_counts())

print('\nCriando 3 categorias com extremos definidos, ROTULADAS')
srCat3= pd.cut(srIdades, bins=[0,30,55,srIdades.max()] ,
               labels=['JUNIOR','EXPERIENTE','SENIOR'])
print(srCat3)


print('\nTabela de Freq das categorias')
srTabFreqCatId= srCat3.value_counts()
print(srTabFreqCatId)


################################
#####        Graficos      #####
################################
# Visualizacao da Parte2
print('\nSeries considerada:')
print(srIdades)
print('\nGrafico de Barras')
srIdades.plot.bar(title='Idades',
                  figsize=(5,3),
                  color=['blue','orange','red'])
plt.show()


print('\nGrafico de Barras Horizontal')

srIdades.plot.barh()
plt.show()

print('\nGrafico de Pizza da Tab de Freq Percentual de categorias de idade')
srTabFreqCatId.plot.pie(title= 'Tab Perc de Cat de Idades',
                        autopct='%.1f')
plt.show()
'''
################################
################################

#---------------------------------------------------------------
#---------------------------------------------------------------
#                      PARTE 3
# Trabalhando com uma series criada a partir de um arquivo excel:
# arquivo comprasabril.xlsx: com as compras feitas pelos clientes 
# em uma determinada loja no mes de abril
# O arquivo deve estar na mesma pasta que o .py
# Coluna 0 servira de indice (index_col=0)
# O arquivo tem linha de cabecalho (header=0)

srClientes = pd.read_excel('comprasabril.xlsx', index_col=0, header=0,
                           squeeze= True)
print('\n srClientes')
print(srClientes)

# Observe a repeticao de indices
# Observe os valores com NaN

# Exiba devidamente identificados:
#  os Indices
#  os Valores
#
#  as compras da emma
#  as compras do vava e nena

#  a series sem os elementos com valor NaN (sem alterar) => .dropna()
#  a series original ordenada pelas compras
#  o nome das pessoas que fizeram as 10 compras de mais alto valor 
#  (considerando as compras separadas mesmo)

print('---')
print(srClientes.index)
print('---')
print(srClientes.values)
print('---')
print(srClientes.loc['emma'])
print('---')
print(srClientes.loc[['vava', 'nena']])

print('\nSeries sem valores ausentes')
print(srClientes.dropna())


##################################
print('\n------------------------------')
# OBSERVE que há repetição de índices: cabem outras outras perguntas
print('\nQuantos são os clientes distintos?')
print(srClientes.index.nunique())

print('\nQuais são os clientes distintos?')
print(srClientes.index.unique().values)



print('\nQt total de compras')
print(srClientes.size)

print('\nQuantas compras cada clientes fez?')
print(srClientes.index.value_counts())

print('Qt total de compras validas')
print(srClientes.count())

print('\nQuantas compras validas cada clientes fez?')
print(srClientes.dropna().index.value_counts())


################################
print('\n------------------------------')

print('\nQual o valor da maior compra (individual)')

print('\nQuanto a loja arrecadou em abril?')


print('\nQuanto cada cliente gastou em abril')
# Warning: sera´ descontinuada 

print('\nQual o maior valor gasto por cliente')
# Warning: sera´ descontinuada 


