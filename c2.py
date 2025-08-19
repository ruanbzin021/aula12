class Carro:
    def __init__(self, marca, nome) -> None:
        self.marca = marca
        self.nome = nome
    def acelerar(self):
        print(f"O {self.nome} está acelerando...")
        
modelo = Carro("Honda", "Civic")
print("Marca:",modelo.marca, "\nNome:",modelo.nome)
modelo.acelerar()

modelo = Carro("BYD", "Dolphin")
print("Marca:",modelo.marca, "\nNome:",modelo.nome)
modelo.acelerar()     