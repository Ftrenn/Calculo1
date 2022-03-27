from math import pi, sqrt

def problema1():

    V = int(input("Volume da lata: "))
    X = int(input("Custo da base e topo por m2: "))
    Y = int(input("Custo da lateral por m2: "))
    X = (X / 10000)
    Y = (Y / 10000)
    
    def raio():
        return ((V/(2*pi))**(1/3))

    def altura():
        return ((4*V/pi)**(1/3))

    def area():
        return (2*pi*raio() * altura() + 2*pi*raio()**2)

    def custo():
        return (X * 2 * (pi * raio()**2) + Y * 2 * pi * raio() * altura())

    def saida():
        print()
        print("=" * 50)
        print()
        print(f"Raio: {raio():.3f} cm\nAltura: {altura():.3f} cm\nÁrea: {area():.3f} cm2\nCusto: R$ {custo():.2f}")
        return
    
    saida()
    return

def problema2():

    X = int(input("Velocidade da barca em km/h: "))
    Y = int(input("Velocidade do carro em km/h: "))
    def funcao(var):
        if var > 0:
            return (sqrt(40**2 + (100-var)**2) / X) + var / Y

    def derivada():
        a = X**2 - Y**2
        b = (X**2 * -200) - (Y**2 * -200)
        c =  (X**2 * 40**2) + (X**2 * 100**2) - (Y**2 * 100**2)

        D = (b**2 - 4*a*c)
        x1 = ((-b + D**(1/2)) / (2*a))
        x2 = ((-b - D**(1/2)) / (2*a))

        lista = (x1, x2)
        return lista

    def pontoMinimo():
        x1, x2 = derivada()
        if funcao(x1-1) > funcao(x1) and funcao(x1+1) > funcao(x1): return x1
        else: return x2

    def distanciaTotal():
        estacao_ate_cidade = sqrt(40**2 + (100 - pontoMinimo())**2) # Distância da barca
        total = estacao_ate_cidade + pontoMinimo() # Distância da barca + distância do carro
        return total

    def saida():
        print()
        print("=" * 50)
        print()
        print(f"Distância da estação até a cidade: {pontoMinimo():.3f} km")
        print(f"Distância total: {distanciaTotal():.3f} km")

    saida()
    return

problema1()
problema2()

