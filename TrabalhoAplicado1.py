"""
Programa que verifica a existência de soluções de funções contínuas através do Teorema do Valor Intermediário

    Primeiramente, o algoritmo recebe duas entradas de números reais que representam os 
limites do intervalo definido pelo usuário, e em seguida calcula o valor de f(x) para estes valores e 
os armazena em suas respectivas variáveis. Posteriormente, o algoritmo calcula o produto entre os 
valores de f(x) para verificar se há uma solução no intervalo, caso exista o programa continua a sua 
execução, senão retorna uma mensagem para o usuário e encerra.

    Na segunda parte do programa o intervalo contendo a solução da função é aproximado até 
obter precisão de 1/10, e para isso cada extremo do intervalo é comparado com a média destes, 
verificando se a solução se encontra no intervalo inferior ou superior à média e em seguida 
descartando a metade do intervalo que não contém a média.

"""

def calculolimite():

    digit = []
    y = []
    intrmax = []
    intrmin= []

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
            intrmax.append((digit[1] + digit[0])/2)
            for i in range(20):
                intrmax.append((intrmax[i] + digit[1])/2)
                intrmax.append((intrmax[i] + digit[0])/2)
            for i in range(20):
                intrmax.append((intrmax[i] + digit[0])/2)
                intrmax.append((intrmax[i] + digit[1])/2)
            [print(n) for n in intrmax]
            print("=" *50)
            [print(n) for n in intrmin]


    valores()
    calculoDosPontos()

calculolimite()