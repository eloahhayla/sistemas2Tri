# from nomeDoArquivo import nomeDaClasse
from conta import Conta

conta1 = Conta(123, "10500-10", "Márcio", 15000.0, 1234)
print(f"saldo em conta corrente: {conta1.extrato()}")

# Criar o saque e o depósito na classe
print(f"saque da conta corrente: {conta1.extrato()}")