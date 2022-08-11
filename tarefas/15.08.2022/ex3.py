'''
Author: @Marcos_Vinicius_Araujo

created_at: 11/08/2022
'''

def ex1():
    
    with open('minhaslembrancas.txt', 'r') as f:
        file = f.read()

    print(file)

def ex2():

    with open('minhaslembrancas.txt', 'r') as f:
        
        for linha in f:
            print(linha, end='\n\n')
        

def ex3():

    with open('minhaslembrancas.txt', 'r') as f:
        file = f.read()
    
    print(f"Numero de frases: {file.count('.')}")

def ex4():

    with open('minhaslembrancas.txt', 'r') as f:
        file = f.read()

    print(len(file.strip().split(' ')))
    