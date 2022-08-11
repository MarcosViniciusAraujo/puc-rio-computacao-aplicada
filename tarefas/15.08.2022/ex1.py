'''
Author: @Marcos_Vinicius_Araujo

created_at: 11/08/2022
'''

def ex1():

    nome = input('Digite seu nome: ')
    n1 = float(input('Digite sua primeira nota: '))
    n2 = float(input('Digite sua segunda nota: '))
    media = (n1 + n2)/2

    print('''
        Nome: {}
        Média: {}
        Situação: {}
    '''.format(
        nome,
        media,
        "Aprovado" if media > 5 else "Reprovado"
    ))

def ex2():
    for i in range(5):
        ex1()

def ex3():
    while True:
        nome = input('Digite seu nome: ')
        
        if nome == '':
            break
    
        n1 = float(input('Digite sua primeira nota: '))
        n2 = float(input('Digite sua segunda nota: '))
        media = (n1 + n2)/2

        print('''
            Nome: {}
            Média: {}
            Situação: {}
        '''.format(
            nome,
            media,
            "Aprovado" if media > 5 else "Reprovado"
        ))