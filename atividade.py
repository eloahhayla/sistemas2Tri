class Quarto:
    def __init__(self, numero, tipo, preco, disponivel):
        self.__numero = numero
        self.__tipo = tipo
        self.__preco = preco
        self.__disponivel = disponivel
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def preco(self):
        return self.__preco

    @property
    def disponivel(self):
        return self.__disponivel

    def exibir_detalhes(self):
        print(f"Numero do quarto: {self.__numero}")
        print(f"Tipo: {self.__tipo}")
        print(f"Preço: {self.__preco}")
        if self.__disponivel:
            print("Quarto livre")
        else:
            print("Quarto ocupado")


quarto1 = Quarto(101, "solteiro", 200.0, True)
quarto1.exibir_detalhes()