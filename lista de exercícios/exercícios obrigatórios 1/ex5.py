import random

def read_bets(filename):
    apostas = {} # {Nome_do_jogador: [apostas...], ...}


    with open(filename, 'r') as f:

        for linha in f:
            linha = linha.strip().split(',')
            it = int(linha[-1])
            nome = linha[0]

            for _ in range(it):
                if apostas.get(nome) == None:
                    apostas[nome] = [f.readline().strip().split(',')]
                else:
                    apostas[nome].append(f.readline().strip().split(','))

    return apostas


# Simular sorteio