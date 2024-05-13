menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMETE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao =="d":
        valor = float(input("Informe o valor do deposito:"))
        if valor > 0 :
            saldo += valor
            print(f"Deposito : RS$ {valor:.2f}\n Novo saldo :{saldo:.2f} ")
        else :
            print("A opereção falhou, valor digitado está incorreto.")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMETE_SAQUES
        if excedeu_saldo:
            print("Saldo insuficente.")
        elif excedeu_limite:
            print("Valor limite de saque excedido, operação não realizada")
        elif excedeu_saque:
            print("Excedeu o limite de saque diario, operação não realizada.")
        elif valor > 0:
            saldo -= valor
            print(f"Saque : R${valor:.2f}\n Novo saldo :{saldo:.2f} ")
        else :
            print("O valor informado é invalido, operação não realizada")
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "q":
        break
    else:
        print("Informe uma opção valida.")