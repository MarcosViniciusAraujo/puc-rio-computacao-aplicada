'''
Author: @Marcos_Vinicius_Araujo

created_at: 11/08/2022
'''

class Cliente:
    def __init__(self, nome, idade, cpf):
        self.nome=nome
        self.idade = idade
        self.cpf = cpf
        self.valorTotalDeCompras=0.0
    
    def __str__(self):
        return ('{}-{}-{}-{}'.format(self.nome,
    self.idade,self.cpf,self.valorTotalDeCompras))

    def __repr__(self):
        return ('{}-{}-{}-{}'.format(self.nome,
    self.idade,self.cpf,self.valorTotalDeCompras))

    def novaCompra(self, valorCompra):
        self.valorTotalDeCompras+=valorCompra

    def informarValorTotalDeCompras(self):
        return self.valorTotalDeCompras
    
    def __lt__(self,outroCli):
        return self.nome < outroCli.nome

class Loja:

    nome:str
    gerente:str
    cnpj:str
    clients:list = []

    def __init__(self, nome:str, gerente:str, cnpj:str) -> None:
        self.nome = nome
        self.gerente = gerente
        self.cnpj = cnpj
    
    def __str__(self) -> str:
        return "Nome: {}\nGerente responsável: {}\nCNPJ: {}".format(
            self.nome,
            self.gerente,
            self.cnpj
        )
    
    def incluiCliente(self, cliente:Cliente) -> None:
        self.clients.append(cliente)
    
    def exibeClientes(self) -> None:
        for cliente in self.clients:
            print(cliente)
    
    def calculaValorTotal(self) -> float:
        return sum([cliente.valorTotalDeCompras for cliente in self.clients])
    

class ClientePreferencial(Cliente):

    percentualDesconto:int

    def __init__(self, nome:str, idade:int, cpf:str, percentualDesconto:int):
        super().__init__(nome, idade, cpf)
        self.percentualDesconto = percentualDesconto
    
    def __str__(self):
        return "Nome: {} - Idade: {} - CPF: {}\n\tDesconto: {}".format(
            self.nome,
            self.idade,
            self.cpf,
            self.percentualDesconto
        )

    def novaCompra(self, valorCompra):
        self.valorTotalDeCompras+=valorCompra * (1 - self.percentualDesconto/100)

c1=Cliente('Vik',34,'1234')
c2=Cliente('Ana',40,'4567')
c1.novaCompra(1500)
c2.novaCompra(2000)
c1.novaCompra(700)
print(c1)
print(c2)
lj = Loja('MAGAZINE','dudu','9999')
print(lj)
lj.incluiCliente(c1)
lj.incluiCliente(c2)
lj.incluiCliente(Cliente('Edu',55,'3456'))
print(lj)
lj.exibeClientes()
print('Total da loja: ',lj.calculaValorTotal())
cp= ClientePreferencial('GUGA',38,'9876',20)
print(cp)
cp.novaCompra(1000)
print(cp)

