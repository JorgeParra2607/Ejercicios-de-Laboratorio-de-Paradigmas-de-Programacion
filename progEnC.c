#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define size 1000

void numAleatorios(int arreglo[]);
void imprimirArreglo(int arreglo[]);
int busquedaSecuencial(int arreglo[], int valor, int tam);
void ordenarArreglo(int arreglo[], int tam);

int main(){

    int arreglo[size];
    int numeroBuscado;

    numAleatorios(arreglo);

    printf("\nEl arreglo generado es: \n");
    imprimirArreglo(arreglo);

    printf("\n\nIngrese el numero que desee buscar (menor a 1000): ");
    scanf("%d", &numeroBuscado);

    //Busqueda Secuencial

    int indice= busquedaSecuencial(arreglo, numeroBuscado, size);

    if(indice != -1){

        printf("\nEl valor %d se encuentra en el indice %d.\n", numeroBuscado, indice);
    }

    else{
        printf("\nEl valor %d no se encuentra en el arreglo.\n", numeroBuscado);
    }

    ordenarArreglo(arreglo, size);

    printf("\nArreglo ordenado: ");
    imprimirArreglo(arreglo);

    printf("\nIngrese nuevamente el numero que desea buscar en el arreglo ordenado: ");
    scanf("%d", &numeroBuscado);

    //Busqueda Secuencial en el arreglo ordenado

    indice= busquedaSecuencial(arreglo, numeroBuscado, size);

    if(indice != -1){

        printf("\n\nEl valor %d se encuentra en el indice %d del arreglo ordenado.\n", numeroBuscado, indice);
    }

    else{

        printf("\n\nEl valor %d no se encuentra en el arreglo ordenado.\n", numeroBuscado);
    }

return 0;
}

// Funcion que genera numeros aleatorios

void numAleatorios(int arreglo[]){
    clock_t inicio= clock(); // Inicia medicion de tiempo

    srand(time(NULL));
    for(int i=0; i<size; i++){

        arreglo[i]= rand() % 1000;
    }

    clock_t fin= clock(); // Finaliza medicion de tiempo
    double tiempo= (double)(fin - inicio) / CLOCKS_PER_SEC; // Calcula el tiempo en segundos
    printf("\nTiempo de generacion del arreglo: %.6f seg\n", tiempo);
}

// Funcion que imprime el arreglo

void imprimirArreglo(int arreglo[]){
    clock_t inicio= clock();

    for(int i=0; i<size; i++){

        printf("%d, ", arreglo[i]);
    }

    printf("\n");

    clock_t fin= clock();
    double tiempo= (double)(fin - inicio) / CLOCKS_PER_SEC;
    printf("\nTiempo de impresion del arreglo: %.6f seg\n", tiempo);
}

//Funcion de busqueda secuencial

int busquedaSecuencial(int arreglo[], int valor, int tam){
    clock_t inicio= clock();

    for(int i=0; i<tam; i++){

        if(arreglo[i] == valor){

            return i;
        }

    }

    clock_t fin= clock();
    double tiempo= (double)(fin - inicio) / CLOCKS_PER_SEC;
    printf("\nTiempo de busqueda secuencial: %.6f seg\n", tiempo);

    return -1;
}

// Funcion que ordena el arreglo generado anteriormente

void ordenarArreglo(int arreglo[], int tam){
    clock_t inicio= clock();

    for(int i = 0; i < tam - 1; i++){

        int min_idx = i;

        for(int j = i + 1; j < tam; j++){

            if (arreglo[j] < arreglo[min_idx]) {
                min_idx = j;
            }
        }

        int temp = arreglo[min_idx];
        arreglo[min_idx] = arreglo[i];
        arreglo[i] = temp;
    }

    clock_t fin= clock();
    double tiempo= (double)(fin - inicio) / CLOCKS_PER_SEC;
    printf("\nTiempo de ordenacion del arreglo: %.6f seg\n", tiempo);

}

// Parra Hernández Jorge Antonio 3CV1
