from conta import Conta

conta1 = Conta(123,"10-1", "Marcinho", 5000, 1234)
conta2 = Conta(123,"10-2", "Joaninha", 200, 1234)

conta1.pix(200,conta2)
print(conta1.extrato())
print(conta2.extrato())