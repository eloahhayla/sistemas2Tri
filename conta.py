class Conta:
    # método construtor
    def __init__(self, agencia, numero, titular, saldo, senha):
        # criando os atributos da classe
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha
        
    def extrato(self):
        return self.__saldo
    
    def sacar(self, valor):
        if self.__saldo >= valor and valor > 0:
            self.__saldo -= valor
            return True
        else:
            return False