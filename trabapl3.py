def area_sob_curva():

    a = float(input("reta a: "))
    b = float(input("reta b: "))
    n = int(input("qtd. de subintervalos: "))

    def funcao(var):
        return 2.718**(-2*var) + 2

    #Tamanho do intervalo
    intervalo = (b - a)
    #Tamanho do subintervalo
    delta_x = intervalo / n

    #Valores de x para extremos esquerdo e direito dos subintervalos
    intervalos_esq = []
    intervalos_esq.append(a)
    intervalos_dir = []
    intervalos_dir.append(a + delta_x)

    for i in range(1, n):
        intervalos_esq.append(intervalos_esq[i-1] + delta_x)
        intervalos_dir.append(intervalos_dir[i-1] + delta_x) 
    
    #Função aplicada aos extremos dos subintervalos
    soma_dir = 0
    soma_esq = 0
    for i in range(n):
        soma_esq += funcao(intervalos_esq[i]) * delta_x
        soma_dir += funcao(intervalos_dir[i]) * delta_x
        
    if soma_dir > soma_esq:
        print(f"A área está entre {soma_esq:.3f} e {soma_dir:.3f}")
    else:
        print(f"A área está entre {soma_dir:.3f} e {soma_esq:.3f}")


area_sob_curva()

