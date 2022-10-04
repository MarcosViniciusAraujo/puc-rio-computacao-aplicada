class Ponto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return "X: {} Y:{}".format(
                self.x,
                self.y
            )
    
    def __add__(self, other):
        return Ponto(self.x + other.x, self.y + other.y)



p1 = Ponto(1, 2)
p2 = Ponto(4, 5)

soma = p1 + p2
print(p1, p2, soma)
print(type(soma))


