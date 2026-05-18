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