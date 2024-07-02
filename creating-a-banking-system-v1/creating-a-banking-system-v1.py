menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        valor = float(input("""
OPÇÃO SELECIONADA: Deposito.
                      
Quanto você deseja depositar? R$"""))
        if valor > 0:
            if valor > 0:
                saldo += valor
                extrato += f"   Depósito de R${valor:.2f}\n"
            
            else:
                print("Operação inválida! Este valor não é válido.")
        
        
    elif opcao.lower() == "s":
        valor = float(input("""
OPÇÃO SELECIONADA: Saque.
                        
Quanto você deseja Sacar? R$"""))
        if saldo > 0:
            if valor > saldo:
                print("""
Não é possível sacar o dinheiro por falta de saldo!""")
                
            elif valor > limite:
                print("""
O valor do saque excedeu o limite de saque!""")
            
            elif numero_saques >= LIMITE_SAQUES:
                print("""
A quantidade de saques excedeu o limite!""")
            else:
                saldo -= valor
                extrato += f"""   Saque de R${valor:.2f}\n"""
                numero_saques += 1
            
        else:
            print("\nOperação inválida! Este valor não é válido.")
    
    elif opcao.lower() == "e":
        print("\n===================== EXTRATO ======================")
        if not extrato:
            print(" Não foram realizadas movimentações na conta.")
        else:
            print(extrato)
            print(f"\n   Saldo: R${saldo:.2f}")
        print("====================================================")
    
    elif opcao.lower() == "q":
        break
    
    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")
