# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:46:58 2022

@author: joisa
"""

print('\n****************************************')
print('**   PARTE1: Exemplo de Dicionario    **')
print('****************************************')
# Exemplo  de dicionário

dAlunoNota = {'lulu': 9.3,  'nana': 7.6, 'vivi': 7.1,
              'tata': 5.8,  'dede': 6.6, 'ziza': 9.1}


print(' Dicionário com CHAVE: nome e VALOR: nota ')
print(dAlunoNota)
print('----------------------------------------')
print('----------------------------------------')
print('  CHAVES do dicionário  ')
print(dAlunoNota.keys())
print('----------------------------------------')
print('----------------------------------------')
print('  VALORES do dicionário  ')
print(dAlunoNota.values())
print('----------------------------------------')
print('----------------------------------------')
print('  VALORES do dicionário  ')
print(dAlunoNota.values())
print('----------------------------------------')
print('----------------------------------------')
print('  ELEMENTOS do dicionário  ')
print(dAlunoNota.items())
print('----------------------------------------')
print('----------------------------------------')
print('Qual a nota do dede?')
# Obter a nota SEM BUSCAR o dede: acessar o dic com a chave (nome)
print(dAlunoNota['dede'])


print('\n****************************************')
print('**  PARTE2: Exercicios de Dicionario   **')
print('****************************************')
print('----------------------------------------')
print('----------------------------------------')
print('Qual a nota da nana?')

print(dAlunoNota['nana'])

print('----------------------------------------')
print('----------------------------------------')
print('Exiba o nome do aluno de maior nota, entre lulu e ziza:')

print("lulu" if dAlunoNota['lulu'] > dAlunoNota['ziza'] else "ziza")

print('----------------------------------------')
print('----------------------------------------')
dProdPreco= {'sabonete':4.6, 'xampu':18.5, 'chinelo':47.5 ,
             'gorro': 23.90, 'casaco':61.90, 'caneta':7.5 ,
             'gaveteiro':181.90, 'mouse':24.5}

print('----------------------------------------')
print('----------------------------------------')
print('Dicionario de produtos e seus precos')
# ESCREVA CÓDIGO AQUI
print(dProdPreco)
print('----------------------------------------')
print('----------------------------------------')
print('Preco do casaco')
# ESCREVA CÓDIGO AQUI
print(dProdPreco['casaco'])

print('----------------------------------------')
print('----------------------------------------')
lProdDesejados = ['caneta','gorro','xampu','mouse']
# ESCREVA  AQUI código para percorrer a lista de 
# produtos desejados acima, e, usando o dicionário 
# dProdPrec, calcular e exibir o valor total a 
# ser pago pelos produtos

preco_a_ser_pago = sum([preco for produto, preco in dProdPreco.items() if produto in lProdDesejados])    
print('Lista de produtos desejados:', lProdDesejados)
print('Valor total a ser pago:', preco_a_ser_pago)
 


