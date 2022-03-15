from math import pi

def problema1():

    V, X, Y = [int(d) for d in input().split()]
    X = X/10000
    Y = Y/10000
    
    def raio():
        return ((V/(2*pi))**1/3)

    def altura():
        return ((4*V/pi)**1/3)

    def area():
        return ((2*pi*raio() * altura()) + 2*(pi*(raio()**2)))

    def custo():
        return (X * (4*pi*raio()) + Y * 2*pi*raio() * altura())

    def resultado():
        print(f"{raio():.2f}, {altura():.2f}, {area():.2f}, {custo():.2f}")
        return
    
    resultado()
    return


def problema2():

    X, Y = [int(d) for d in input().split()]

    def derivada():
        # Retorna o ponto em que f''(x) = 0
        a = (X**2) + (Y**2)
        print(a)
        b = (Y**2 * 200) + (X**2 * 200)
        print(b)
        c = (Y**2 * 100**2) + (X**2 * 40**2) + (X**2 * 100**2)
        print(c)

        D = (b**2 - 4*a*c)
        print(D)
        x1 = (-b + D**(1/2)) / (2*a)
        x2 = (-b - D**(1/2)) / (2*a)

        print(f'\nValor de x1: {x1}')
        print(f'Valor de x2: {x2}')

    derivada()

problema2()