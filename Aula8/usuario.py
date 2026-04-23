class Usuario:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
    
    @property # Get
    def nome(self):
        return self._nome
    
    @nome.setter # Set
    def nome(self, valor):
        self._nome = valor