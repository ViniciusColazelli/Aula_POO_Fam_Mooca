#class Conta:
    #def __init__(self):
        #self._saldo = 1000
    
    #def saldo(self):
        #return self._saldo

#conta = Conta()

#print(conta._saldo)

#conta._saldo = 2000 # isso é proibido pro convenção

#print(conta._saldo)

#----------------------------------------------------------

# class Conta:
#     def __init__(self):
#         self.__saldo = 1000

#     @property
#     def saldo(self):
#         return self.__saldo

# conta = Conta()

# print(conta.saldo)

# conta.__saldo = 2000

# print(conta.saldo)

#-----------------------------------------------------------

from dataclasses import dataclass

@dataclass(frozen=True)
class Conta:
    saldo: float = 1000
    nome: str = "Maria"

conta = Conta()

print(conta.saldo)
print(conta.nome)

# Isso da erro
# conta.saldo = 5000 # Vai dar um FrozenInstanceError!