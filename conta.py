conta1 = criaConta(321, "02002-0", "Hayssa", 100.0, 1000, 3202)
print(f"Agência: {conta1['agencia']}, Conta: {conta1['numero']} - SALDO: {conta1['saldo']}") 

conta2 = criaConta(123, "2000-2", "Márcio", 15000.0, 50000, 2023)
print(f"Agência: {conta2['agencia']}, Conta: {conta2['numero']} - SALDO: {conta2['saldo']}") 

class Conta:
    # método construtor
    def __init__(self, agencia, numero, titular, saldo, senha):
        # criando os atributos da classe
        # atributo privado usa 2 underlines
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha
        
    def extrato(self):
        return self.__saldo
    
    def saque(self, valor):
        if self.__saldo >= valor and valor > 0:
            self.__saldo -= valor
            return True
        else:
            return False
    
    def deposito(self, valor):
        if valor > 0:
            self.__saldo += -valor
            return True
        else:
            return False
        
    def pix(self, valor, conta):
        if self.__saldo >= valor and valor > 0:
            self.__saldo -= valor
            conta.__saldo += valor
            return True
        else:
            return False