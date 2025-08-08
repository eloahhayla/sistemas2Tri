class Quarto:
    def __init__(self, numero, tipo, preco, disponivel):
        self.__numero = numero
        self.__tipo = tipo
        self.__preco = preco
        self.__disponivel = disponivel

    def exibir_detalhes(self):
        print(f"Numero do quarto: {self.__numero}")
        print(f"Tipo: {self.__tipo}")
        print(f"Preço: {self.__preco}")
        if self.__disponivel:
            print("Quarto livre")
        else:
            print("Quarto ocupado")
    
    def reservar(self):
        if self.__disponivel == True:
            self.__disponivel = False
            print(f"Reserva efetuada")
        else:
            print("Não foi possivel reservar, quarto ocupado.")

    def liberar(self):
     if self.__disponivel == False:
        self.__disponivel = True
        print(f"Tá liberado pra ser reservado")
     else:
        print("Reservado com sucesso!!!!!!!!!!!!!")
            
