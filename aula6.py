class Veiculo:
    def __init__(self, marca):
        self.marca = marca
    
    def mover(self):
        return "Está se movendo"

class Carro(Veiculo):
    def mover(self):
        return "O carro está dirigindo na estrada"
    
class Bicicleta(Veiculo):
    def mover(self):
        return "A bicicleta está sendo pedalada"
    
c = Carro("Honda")
b = Bicicleta("Caloi")

print(c.marca, "→", c.mover())
print(b.marca, "→", b.mover())

#---------------------------------------------------------
print(45 * "-")
#---------------------------------------------------------

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

e = Estudante("Vinicius", "19", "123456")

print(f"{e.nome} tem {e.idade} anos → matricula: {e.matricula}")

#---------------------------------------------------------
print(45 * "-")
#---------------------------------------------------------

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        return "Som genérico de animal"
    
    def descrever(self):
        return f"Eu sou {self.nome}, tenho {self.idade} anos"
    
class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca
    
    def fazer_som(self):
        return "Au au au!"

class Gato(Animal):
    pass

rex = Cachorro("Rex", 4, "Labrador")

print(rex.descrever())
print(rex.fazer_som())
print(f"Rex é da raça: {rex.raca}")
print()

print("rex é instância de Cachorro?", isinstance(rex, Cachorro))
print("rex é instância de Animal?", isinstance(rex, Animal))
print("rex é instância de Gato?", isinstance(rex, Gato))

#---------------------------------------------------------
print(45 * "-")
#---------------------------------------------------------

class A: pass
class B: pass
class C(A, B): pass

print(C.__mro__)

#---------------------------------------------------------
print(45 * "-")
#---------------------------------------------------------

