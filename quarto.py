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
            print("Quarto liberado")
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
        print(f"Quarto liberado")
     else:
        print("Quarto reservado com sucesso!")

    def alterar_preco(self, preco):
        self.__preco = preco
        print(f"Preço novo: {self.__preco}")