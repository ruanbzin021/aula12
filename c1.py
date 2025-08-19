class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa("André", "Marques")
p2 = Pessoa("Ruan", "Barros")
print(p1.nome)
print(p2.nome)