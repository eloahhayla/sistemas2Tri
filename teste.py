import random
from conta import Conta

while True:
    print("\nCadastro de Conta")
    agencia = input("Agência: ")
    numero_conta = random.randint(10000, 99999)
    titular = input("Titular: ")
    saldo = float(input("Saldo: "))
    senha = input("Senha: ")

    conta = Conta(agencia, numero_conta, titular, saldo, senha)
    
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
    
    continuar = input("Deseja cadastrar outra conta? (s/n): ").lower()
    if continuar != "s":
        break