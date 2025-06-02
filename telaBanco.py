# from nomeDoArquivo import nomeDaClasse
from conta import Conta

conta1 = Conta(123, "10500-10", "Márcio", 15000.0, 1234)
print(f"saldo em conta corrente: {conta1.extrato()}")

# Sacando Valor
if conta1.sacar(8):
    print("Saque efetuado com sucesso!")
else