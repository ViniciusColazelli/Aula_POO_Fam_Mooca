#Polimorfismo parametrico
from typing import TypeVar, Generic

T = TypeVar("T")

class Caixa(Generic[T]):
    def __init__(self, item: T):
        self.item = item
    
    def pegar_item(self) -> T:
        return self.item

if __name__ == "__main__":
    caixa_int = Caixa[int](42)
    caixa_str = Caixa[str]("Python")
    caixa_lista = Caixa[list]([1, 2, 3])

    print(caixa_int.pegar_item())
    print(caixa_str.pegar_item())
    print(caixa_lista.pegar_item())

#------------------------------------------------------
print("-" * 45)
#------------------------------------------------------

#Correção de Tipos (Type Coercion)
print(5 + 3,14)         # int é convertido para float automaticamente
print("Idade: " + str(25))  # int convertido para str

#Outro Exemplo
def repetir(texto, vezes):
    return texto * vezes

print(repetir("Python ", 3))

#------------------------------------------------------
print("-" * 45)
#------------------------------------------------------

class Animal:                               #Sobrescrita (Overriding)
    def fazer_som(self):
        print("O animal faz um som...❓") 

class Cachoro(Animal):
    def fazer_som(self):
        print("🐶 Au Au Au!")
    
class Gato(Animal):
    def fazer_som(self):
        print("😺 Miau Miau!")
    
class Vaca(Animal):
    def fazer_som(self):
        print("🐮 Muuuu!")


#Polimorfismo de Inclusão
def fazer_barulho(animal: Animal):
    animal.fazer_som()    #Chama o método correto de cada subclasse

#Testando
animais = [Cachoro(), Gato(), Vaca(), Animal()]

for animal in animais:
    fazer_barulho(animal)

#------------------------------------------------------
print("-" * 45)
#------------------------------------------------------

#Polimorfismo de Sobrecarga
class Calculadora:
    def somar(self, a, b=None):
        if b is None:
            return a + a
        return a + b

if __name__ == "__main__":
    calc = Calculadora()
    print(calc.somar(5))    #10
    print(calc.somar(5, 3)) #8