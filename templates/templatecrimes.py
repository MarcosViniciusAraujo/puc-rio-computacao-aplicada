# -*- coding: utf-8 -*-
"""
NOME:
TURMA:
    
Crimes 2022
"""



'''
No arquivo crimeszs.xlsx encontram-se registrados os crimes cometidos na zona
sul na ultima sexta-feira.
Cada linha tem: bairro onde foi cometido o crime e tipo do crime cometido
'''

'''
1- Crie e exiba uma series a partir do arquivo crimeszs.xlsx, deixando os bairros 
como indices
'''
print('\n1- Series dos crimes')


'''
2- Valores Nan devem ser preenchidos com "NAO ESPECIFICADO'.
   Exiba  a series resultante
'''
print('\n2- Com Valores NaN  preenchidos com "NAO ESPECIFICADO"')



'''
3- Exiba o numero total de crimes .
   Exiba  a series resultante
'''
print('\n3-Numero total de crimes')



'''
4- Crie agora a tabela de frequencia dos crimes (srTabFreqCrimes).
Exiba a tabela
'''
print('\n4- Tabela de Frequencia dos Crimes')



'''
5- Tabela de Frequencia e Tabela de Frequencia Relativa
(tambem chamada Tabela de Frequencia Percentual):
A tabela de frequencia relativa e´ obtida considerando-se 
o total.
Por exemplo: se o numero de homicidios for 12 e o numero 
total de crimes for 40, homicidios sao 30% dos crimes.
Uma possibilidade para obter a (series) Tabela de Frequencia 
Relativa é fazer :
srTabFreqRel = srTabFreq*100/srCrimes.size
Mas podemos também usar o normalize = True em value_counts()
'''
print('\n5-Tabela de Frequencia Relativa dos Crimes')


'''
6- Para deixar os valores com um certo formato, podemos 
aplicar (apply) sobre os valores a funcao '{}'.format
MAS ATENCAO: Nesse caso um outra series e´criada e os 
valores sao armazenados como string
'''
print('\n6- Tabela de Frequencia Relativa dos Crimes formatada')


'''
7- Qual(is) o(s) crime(s) com maior numero de ocorrencias?
   E qual a quantidade de ocorrencias desse(s) crime(s)?
'''

print('\n7.1- Crime(s) com maior numero de ocorrencias')



print('\n7.2- E a quantidade de ocorrencias desse(s) crime(s)')



'''
8- Crie uma series srGavea so com os crimes na GAVEA
'''
'''
8.1- Exiba a series srGavea
'''
print('\n8.1 -Crimes na GAVEA')

'''
8.2- Exiba a quantidade de HOMICIDIO na Gavea
'''
print('\n8.2 Quantidade de HOMICIDIOS na GAVEA')


'''
9- Crie  a series srBOTA so com os crimes em BOTAFOGO
'''
'''
9.1 - Exiba a series srBOTA
'''
print('\n9.1- Crimes em BOTAFOGO')


'''
9.2 - Qual o crime que mais ocorreu em BOTAFOGO'
'''
print('\n9.2- Crime que mais ocorreu em BOTAFOGO')


'''
10 - Exiba a quantidade de crimes por bairro
Precisa de uma dica? Voce pode agrupar por Bairro 
e usar a funcao de agregacao que "conta" a quantidade 
de elementos em cada grupo.
(Mas na prova nao tem dica)
'''
print('\n10- Quantidade de Crimes por Bairro')

'''
11 - Qual(is) o(s) bairro(s) com a maior quantidade de crimes?
'''
print('\n11- Bairro(s) com maior quantidade de crimes')




