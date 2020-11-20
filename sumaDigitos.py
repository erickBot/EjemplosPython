#crea listas vacias
sumaDigitos_ = []
myNumeros = []
nuevosNumeros = []
nuevaSUmaDigitos = []

def nuevaLista(cantidad):
    while cantidad > 0:
        numMin = min(sumaDigitos_)
        indice = sumaDigitos_.index(numMin)
        num = myNumeros[indice]
        nuevaSUmaDigitos.append(numMin)
        nuevosNumeros.append(num)
        sumaDigitos_.remove(numMin)
        myNumeros.remove(num)
        cantidad = cantidad - 1
    print ("Nueva lista ordenada de menor a mayor segun la suma de sus digitos de los numeros originales: ")
    print (nuevosNumeros)
    print ("Suma de digitos de los numeros, ordenada de menor a mayor: ")
    print (nuevaSUmaDigitos)

def run(n):
    i = 1
    cantidad = n
    while cantidad > 0:
        numero = int(input("Ingrese el numero " + str(i) + ": "))
        #agrega elementos a la lista
        myNumeros.append(numero)
        i = i + 1
        cantidad = cantidad -1

    #va a a funcion sumar digitos
    for i in range(n):
        sumaDigitos(myNumeros[i])

    print ("Los numeros originales son: ")
    print (myNumeros)
    print ("La suma de los digitos de los numeros es: ")
    print (sumaDigitos_)

    nuevaLista(n)

def sumaDigitos(num):
    suma = 0
    while num != 0:
        unidad = num % 10
        num = num //10
        suma = suma + unidad
    
    sumaDigitos_.append(suma)

if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de numeros: "))
    run(n)

