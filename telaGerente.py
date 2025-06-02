from conta import Conta

# - Criar um formulário, para o gerente preencher os dados da conta
# - Usar prints e inputs para receber:
# - Agência
# - Número da conta (criar um número aleatório de 5 digitos)
# - Titular
# - Saldo
# - Senha
# - Usar laço de repetição infinito para que o sistema permita cadastrar várias contas
while True:
    print("*Cadastro de Conta*")
    agencia = input("Agência: ")
    senha = input("senha: ")
    titular = input("Titular: ")
    saldo = input("Saldo: ")
    print("*Conta criada!")