from connect import Connect
from usuario import Usuario

if __name__ == "__main__":
    db = Connect()

    lista = [
        Usuario("Marcos", "marcos@email.com"),
        Usuario("Julia", "julia@email.com"),
        Usuario("Pedro", "pedro@email.com"),
        Usuario("Sofia", "sofia@email.com")
    ]

    for p in lista:
        db.inserir(p)

    db. alterar(1, "Marcos Editado")

    print(f"{'ID':<4} | {'NOME':<15} | {'EMAIL'}")
    print("-" * 40)

    for user in db.listar():
        print(f"{user[0]:<4} | {user[1]:<15} | {user[2]}")