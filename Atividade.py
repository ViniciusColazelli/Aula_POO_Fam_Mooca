class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._velocidade = 0

    def acelerar(self):
        self._velocidade += 10
        return f"Velocidade: {self._velocidade} km/h"



class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def acelerar(self):  # Polimorfismo
        self._velocidade += 20
        return f"Carro acelerando: {self._velocidade} km/h"



class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def acelerar(self):  # Polimorfismo
        self._velocidade += 30
        return f"Moto acelerando: {self._velocidade} km/h"


veiculo = Veiculo("Generico", "Base")
carro = Carro("Bugatti", "Chiron", portas = 2)
moto = Moto("Honda", "CB 500", cilindradas = 500)


print("=== Veículo ===")
print(veiculo.acelerar())

print("\n=== Carro ===")
print(carro.acelerar())

print("\n=== Moto ===")
print(moto.acelerar())


print("\n=== Polimorfismo em ação ===")
frota = [veiculo, carro, moto]
for veiculos in frota:
    print(veiculos.acelerar())