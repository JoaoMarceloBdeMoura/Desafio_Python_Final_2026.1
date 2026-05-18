validador = 1

while validador == 1:
    #1. Entrada de Dados e Tipos:
    
    destino = input("Digite o nome da Cidade/País que irá visitar: ")
    print("===================================================")
    valor = float(input("Digite o orçamento disponível em Reais: "))
    if valor >= 0:
        
        orcamento = valor
        print("===================================================")
        valor = float(input("Digite o valor da passagem em Reais: "))
        if valor >= 0:

            passagem = valor
            print("===================================================")
            valor = float(input("Digite o valor da diária em Euros: "))
            if valor >= 0:

                hospedagem = valor
                print("===================================================")
                valor = int(input("Digite a quantidade de dias que irá ficar: "))
                if valor >= 0:

                    dias = valor
                    print("===================================================")
                else:
                    print("Valor inválido")
                    break
            else:
                print("Valor inválido")
                break
        else:
            ("Valor inválido")
            break
    else:
        print("Valor inválido")
        break
                           
    validador = 0

#2. Cálculos e Lógica:
print("\n")
conversao = float(orcamento/6.1)
print(f"Teu orçamento vale {conversao:.2f} Euros kkkkkkkkkkkkk\n")

calc_hospedagem = float(hospedagem*6.1)
gasto_total = float(calc_hospedagem * dias)

#Validação do orçamento
if orcamento < gasto_total:
    print("Não vai dar não man. Orçamento não possível e Não Viável")
    print(f"Te falta {(gasto_total - orcamento):.2f} reais ({(gasto_total - orcamento)/6.1:.2f} euros) para ir em {destino}")
elif orcamento == gasto_total:
    print("Sobra nada pro beta")
else:
    print(f"Vai na fé, te sobra {(orcamento - gasto_total):.2f} reais ({(orcamento - gasto_total)/6.1:.2f} euros) para ir em {destino}. Orçamento possível e Viável")

#3. Exibição de Resultados:

print(f"\nCusto total da viagem: R${(gasto_total)} reais\n")