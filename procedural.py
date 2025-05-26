def criaConta(agencia, numero, titular, saldo, limite, senha):
    conta = {
        "agencia": agencia,
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite,
        "senha": senha
    }
    return conta

conta2 = criaConta(123, "2000-2", "Márcio", 15000.0, 50000, 2023)
print(f"Agência: {conta2['agencia']}, Conta: {conta2['numero']} - SALDO: {conta2['saldo']}") 

conta1 = criaConta(321, "02002-0", "Hayssa", 100.0, 1000, 3202)
print(f"Agência: {conta1['agencia']}, Conta: {conta1['numero']} - SALDO: {conta1['saldo']}") 