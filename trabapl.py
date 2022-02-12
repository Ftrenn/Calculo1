from tokenize import Double


def calculolimite():

    digit = []
    y = []
    intr = []

    def funcao(val):
        return (1/2.718**val) - (2*val**2) + 4


    def valores():
        while True:
            num1 = float(input("Digite o primeiro numero real: "))
            num2 = float(input("Digite o segundo numero real: "))
            
            # Aplica a função:
            total1 = (1/2.718**num1) - (2*num1**2) + 4
            total2 = (1/2.718**num2) - (2*num2**2) + 4

            # Um precisa ser negativo e o outro positivo para o ter solução no intervalo, portanto total1 * total2
            # precisa ser <= 0
            if total1 * total2 > 0:
                print("-- não é possível afirmar que existe solução neste intervalo, tente outros dois números --")
            
            else:
                digit.append(num1)
                digit.append(num2)
                break

    def calculoDosPontos ():
        # Calcula o Y e coloca em difEntreTotais
        for i in range(len(digit)):
            total = (1/2.718**digit[i]) - (2*digit[i]**2) + 4
            y.append(total)

            # Printa o valor de Y para os digit de X digitados
            print(f"f({digit[i]}) = {y[i]:.2f}")

        print("Equação: e(-x) - 2x² + 4 = 0\n")

        diferenca = abs(digit[1] - digit[0])

        if diferenca <= 0.1:
            print("a equação tem pelo menos uma solução neste intervalo")
        else:
            intr = [digit[0], digit[1]]
            intr.append(intr[0] + intr[1]) / 2
            i = 1
            while True:
                if abs(funcao(intr[i]) - funcao(medx)) > abs(funcao(medx) - funcao(intr[i-1])):   
                    intr.append((medx + intr[i-1]) / 2)
                else:
                    intr.append((medx + intr[i]) / 2)
                if abs(intr[i-2] - intr[i-1]) <= 0.1:
                    [print(c) for c in intr]
                    print(f"solucao no intervalo {intr[i-1]}, {intr[i]}")
                    break
                i += 1
                

    valores()
    calculoDosPontos()

calculolimite()