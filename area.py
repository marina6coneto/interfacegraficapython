class Retangulo:
    
    def __init__(self, lado_a, lado_b):
        self.a = lado_a
        self.b = lado_b
        
    def muda_valor(self, novo_a, novo_b):
        self.a = novo_a
        self.b = novo_b

    def retorna_lado(self):
        print(f'O Retângulo possui dimensões {self.a}m x {self.b}m')

    def area(self):
        return self.a * self.b
