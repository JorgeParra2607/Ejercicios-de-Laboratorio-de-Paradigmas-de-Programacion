import random
import time

size = 1000

# Función que genera números aleatorios
def num_aleatorios():
    inicio = time.time() # Inicia medicion de tiempo

    arreglo = [random.randint(0, 999) for _ in range(size)]

    fin = time.time() # Finaliza medicion de tiempo
    tiempo = fin - inicio # Calcula el tiempo en segundos
    print("\nTiempo de generacion del arreglo:", tiempo, "seg")

    return arreglo

# Función que imprime el arreglo
def imprimir_arreglo(arreglo):
    inicio = time.time()

    print(", ".join(map(str, arreglo)))

    fin = time.time()
    tiempo = fin - inicio
    print("\nTiempo de impresion del arreglo:", tiempo, "seg")

# Función de búsqueda secuencial
def busqueda_secuencial(arreglo, valor):
    inicio = time.time()

    for i, num in enumerate(arreglo):
        if num == valor:
            fin = time.time()
            tiempo = fin - inicio
            print("\nTiempo de busqueda secuencial:", tiempo, "seg")
            return i

    fin = time.time()
    tiempo = fin - inicio
    print("\nTiempo de busqueda secuencial:", tiempo, "seg")

    return -1

# Función que ordena el arreglo
def ordenar_arreglo(arreglo):
    inicio = time.time()

    for i in range(len(arreglo) - 1):
        min_idx = i
        for j in range(i + 1, len(arreglo)):
            if arreglo[j] < arreglo[min_idx]:
                min_idx = j
        arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]

    fin = time.time()
    tiempo = fin - inicio
    print("\nTiempo de ordenacion del arreglo:", tiempo, "seg")

def main():
    arreglo = num_aleatorios()

    print("\nEl arreglo generado es:")
    imprimir_arreglo(arreglo)

    numero_buscado = int(input("\nIngrese el número que desea buscar (menor a 1000): "))

    indice = busqueda_secuencial(arreglo, numero_buscado)
    if indice != -1:
        print(f"\nEl valor {numero_buscado} se encuentra en el índice {indice}.")
    else:
        print(f"\nEl valor {numero_buscado} no se encuentra en el arreglo.")

    ordenar_arreglo(arreglo)

    print("\nArreglo ordenado:")
    imprimir_arreglo(arreglo)

    numero_buscado = int(input("\nIngrese nuevamente el número que desea buscar en el arreglo ordenado: "))

    indice = busqueda_secuencial(arreglo, numero_buscado)
    if indice != -1:
        print(f"\nEl valor {numero_buscado} se encuentra en el índice {indice} del arreglo ordenado.")
    else:
        print(f"\nEl valor {numero_buscado} no se encuentra en el arreglo ordenado.")

if __name__ == "__main__":
    main()
