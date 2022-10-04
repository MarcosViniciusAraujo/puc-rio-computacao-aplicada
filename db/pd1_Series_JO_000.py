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

'''
Criando uma series a partir de duas listas:
uma para valores e outra para indices
'''


lpessoas= ['tita','ludo','yuki','zeus','matt','deby','dave','babi', 'lulu']
lprof= ['medico','professor','advogado','filosofo','professor','medico','dentista','professor', 'fisioterapeuta']
lidades= [45,30,67,37,26,58,43,38,29]

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
print('Antes:',srProfissoes.loc['lulu'] )
srProfissoes.loc['lulu']= 'chef'
print('Antes:',srProfissoes.loc['lulu'] )

#Incluir um novo elemento: ruan, medico => .loc[] = ...
#Exibir a series depois da inclusao, assim como o seu tamanho
print('\n Incluindo ruan')
srProfissoes.loc['ruan']= 'medico'
print(srProfissoes)
print('TAM:', srProfissoes.size)

#Apenas exibir a series SEM  yuki, dave => .drop([lista de indices])
print('\n Sem yuki, dave')
print(srProfissoes.drop([ 'yuki', 'dave'])) # COPIA DA SERIES

#Exibir a series srProfissoes 
print('\n Series:')
print(srProfissoes)


#Eliminar da srProfissoes yuki e lulu => .drop([lista de indices], inplace=True)
#Obs: inplace=True altera na própria series
srProfissoes.drop([ 'yuki', 'lulu'], inplace=True)

#Exibir a series srProfissoes atualizada  e o tamanho
print('\n Series atualizada:')
print(srProfissoes)
print('TAM:', srProfissoes.size)

#Apenas exibir a series  srProfissoes ordenada por profissao (valores) => .sort_values()
print('\n Exibicao da Series ordenada por profissao:')
print(srProfissoes.sort_values())

#Ordenar a series pelo nome das pessoas => .sort_index(inplace=True)
#Depois exibir a series alterada
print('\n Series srProfissoes alterada (ordenada por indice) :' )
srProfissoes.sort_index(inplace=True)
print(srProfissoes)


#---------------------------------------------------------------
#---------------------------------------------------------------
#                        PARTE 2
# A partir das listas lpessoas e lidades crie a series srIdades 
# em os valores devem ser as idades e os indices os nomes das pessoas

#Exiba devidamente identificados:
# a series
# os indices
# os valores
# a idade da tita
# os 3 ultimos elementos
# os 7 primeiros elementos da series, ordenados pela idade (nao alterar a series)
# os 3 primeiros mais novos
# a series original sem a babi (nao alterar)


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
#print(srClientes)

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


