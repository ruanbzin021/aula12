class Animal:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade

    def som(self):
        print(f"O {self.nome} está comendo.")
        if self.nome.lower() == "gato":
            print(f"O {self.nome} faz Miauuuuuuu")
        elif self.nome.lower() == "cachorro":
            print(f"O {self.nome} faz AUAU")

a1 = Animal("Gato", 50.0, 10)
print("Nome:", a1.nome, "\nPeso:", a1.peso, "\nIdade:", a1.idade)
a1.som()

print()

a2 = Animal("Cachorro", 20.0, 3)
print("Nome:", a2.nome, "\nPeso:", a2.peso, "\nIdade:", a2.idade)
a2.som()
