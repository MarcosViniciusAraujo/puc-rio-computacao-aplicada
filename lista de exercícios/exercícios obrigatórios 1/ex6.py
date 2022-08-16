

valor_inserido = int(input('Digite o valor arrecadado: '))

montante = []

while valor_inserido > 0:

    montante.append(valor_inserido)

    valor_inserido = int(input('Digite o valor arrecadado: '))


with open('montante.txt', 'a') as f:
    for valor in montante:
        f.write(str(valor) + '\n')

