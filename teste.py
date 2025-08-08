# CÓDIGO PARA TESTE
from quarto import Quarto
quarto1 = Quarto(101, "Solteiro", 500.00, True)
quarto1.exibir_detalhes()
quarto1.reservar()
quarto1.exibir_detalhes()
quarto1.liberar()
quarto1.alterar_preco(5550.00)
quarto1.exibir_detalhes()