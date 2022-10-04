# -*- coding: utf-8 -*-

'''
EX POO: escreva a classe ContaBancaria


Uma conta bancaria tem:
    o numero da conta
    a senha
    o nome do titular da conta
    o saldo da conta

    
Uma conta pode ser criada de duas formas:
    - fornecendo numero, senha, nome e saldo
    - fornecendo apenas, numero, senha e nome. Nesse caso o saldo 
    e´ 0.0  
      ===> __init__  (construtor)
      (OBS: VEJA NOS SLIDES e VÍDEOS ->CONSTRUTOR COM PARÂMETRO DEFAULT !!!)

Ao ser dado um print numa conta sao exibidos numero, nome e saldo
      ===> Método mágico __str__ 


Uma conta bancaria pode:
    - exibir seu saldo, desde que seja recebida a senha 
      correta da conta. Caso a senha recebida seja incorreta 
      exibir mensagem: SENHA INCORRETA
      ===> Método exibeSaldo
      
    - ter um valor depositado, recebendo para isso o valor 
      a ser depositado. O valor deve ser adicionado ao saldo 
      da conta
      ===> Método deposito
      
    - ter um valor sacado, desde que para isso sejam recebidos 
      o valor a ser sacado e a senha da conta.
      Caso a senha seja incorreta, exibir a mensagem  
      SENHA INCORRETA e sinalizar que a operacao nao foi 
      realizada, retornando False.
      Caso o valor a ser sacado seja maior do que o saldo, 
      exibir a mensagem SALDO INSUFICIENTE e sinalizar que a operacao nao foi 
      realizada, retornando False.
      Caso seja possivel realizar o saque, subtrair o valor sacado 
      do saldo da conta e retornar True.
      ===> Método saque
      
 
      Além disso, é possível usar o operador > para comparar duas contas 
      bancárias. Um conta bancária é considerada maior do que outra se 
      seu saldo for  maior do que o saldo da outra 
      ===> Método mágico __gt__ ( análogo ao __lt__  da classe Pessoa 
       visto em aula)
      (OBS: VEJA NOS SLIDES e VÍDEOS -> MÉTODOS MÁGICOS (ESPECIAIS)!!)
      
 
'''
# Escreva a seguir a classe ContaBancaria

class ContaBancaria:

    def __init__(self, num_conta, senha, titular, saldo):
        self.num_conta = num_conta
        self.senha = senha
        self.titular = titular
        self.saldo = saldo

    
    def __init__(self, num_conta, senha, titular):
        self.num_conta = num_conta
        self.senha = senha
        self.titular = titular
        self.saldo = 0.0


    def __str__(self):
        return "Numero: {}\nNone: {}\nSaldo: {}".format(
                self.num_conta,
                self.titular,
                self.saldo
        )

    def exibe_saldo(self, senha):
        if senha == self.senha:
            print('Senha: {}\n'.format(self.saldo))
        else:
            print('SENHA INCORRETA')

    def deposito(self, valor):
        self.saldo += valor


    def saque(self, valor, senha):
        if senha != self.senha:
            print('SENHA INCORRETA')
            return False
        elif valor > self.saldo:
            print('SALDO INSUFICIENTE PARA SER RETIRADO')
            return False
        else:
            self.saldo -= valor
            return True


    def __gt__(self, other):
        return self.saldo > other.saldo
    



# Fim da classe ContaBancaria

##################################################
##################################################
# Bloco Principal
# Retire os # para testar a classe criada por você

c1= ContaBancaria(333,'vaka','LALA',200)
print(c1)

c2= ContaBancaria(888,'aabb','BETO', 3500.50)
print(c2)

c1.exibeSaldo('kkkk')
c1.exibeSaldo('vaka')

print(c1)
c1.deposito(2300)
print(c1)
# print(c2)
# if c1>c2:
#     print('Conta de maior saldo:', c1)
# else:
#     print('Conta de maior saldo:', c2)
    
# c1.saque(450, 'vaka')
# print(c1)

# c3=ContaBancaria(999,'kill','TETE') 
# print(c3)


##################################################
##################################################
# Saída esperada para o código de teste acima:
# 333-LALA-200.00
# 888-BETO-3500.50
# SENHA INCORRETA
# SALDO EM CONTA:  200.00
# 333-LALA-200.00
# 333-LALA-2500.00
# 888-BETO-3500.50
# Conta de maior saldo: 888-BETO-3500.50
# 333-LALA-2050.00
# 999-TETE-0.00    
    
        
        
