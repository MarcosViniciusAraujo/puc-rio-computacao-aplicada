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


def get_random_result():
    result = []

    while len(result) <= 6:
        num_sorteado = random.randint(1, 60)

        if num_sorteado not in result:
            result.append(num_sorteado)
    
    return result



def check_winner(bets, result):

    for bet in bets:
        if bet not in result:
            return False
    return True



# Simular sorteio

GABARITO = get_random_result()

aposta = read_bets('apostas16junho.txt')


for pessoa, bets in aposta.items():
    
    print(f"Jogador: {pessoa}")

    for i,bet in enumerate(bets):
        is_winner = check_winner(bet, GABARITO)
        print(f"Aposta #{i + 1}: {is_winner}")