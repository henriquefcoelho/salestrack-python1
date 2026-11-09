
print("========================================")
print("               SALESTRACK               ")
print("       Sistema de Análise de Vendas      ")
print("========================================")

vendas = []


# Criando menu de interação com o usuário
opção = -1

while opção != 6:
    print("\n========================================")
    print("             MENU PRINCIPAL             ")
    print("========================================")
    print("1 - Registrar vendas")
    print("2 - Consultar faturamento")
    print("3 - Consultar média de vendas")
    print("4 - Consultar maior e menor venda")
    print("5 - Consultar vendas acima da média")
    print("6 - Sair")
    print("----------------------------------------")

    opção = int(input("Digite a opção desejada: "))

    if opção == 1:
        # Registrando as vendas
        print("\n========================================")
        print("           REGISTRO DE VENDAS           ")
        print("========================================")

        for i in range(5):
            valor = float(input("Digite o valor da venda: "))

            # Verificando se o valor é positivo
            while valor < 0:
                print("\nValor inválido! Digite um valor positivo.")
                valor = float(input("Digite o valor da venda: "))

            vendas.append(valor)

        print("\n----------------------------------------")
        print("     Vendas registradas com sucesso!    ")
        print("----------------------------------------")

    elif opção == 2:
        # Calculando faturamento total
        faturamento_total = sum(vendas)

        print("\n========================================")
        print("            FATURAMENTO TOTAL           ")
        print("========================================")
        print(f"Faturamento total: R$ {faturamento_total:.2f}")
        print("----------------------------------------")

    elif opção == 3:
        # Calculando a média de vendas
        media_vendas = faturamento_total / len(vendas)

        print("\n========================================")
        print("             MÉDIA DE VENDAS            ")
        print("========================================")
        print(f"Média de vendas: R$ {media_vendas:.2f}")
        print("----------------------------------------")

    elif opção == 4:
        # Mostrando a maior e a menor venda
        maior_venda = max(vendas)
        menor_venda = min(vendas)

        print("\n========================================")
        print("           ANÁLISE DE VENDAS            ")
        print("========================================")
        print(f"Maior venda: R$ {maior_venda:.2f}")
        print(f"Menor venda: R$ {menor_venda:.2f}")
        print("----------------------------------------")

    elif opção == 5:
        # Analisando as vendas que superaram a média
        vendas_acima_media = [venda for venda in vendas if venda > media_vendas]

        print("\n========================================")
        print("          VENDAS ACIMA DA MÉDIA         ")
        print("========================================")
        print(f"Vendas acima da média: {vendas_acima_media}")
        print("----------------------------------------")

