#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 10

int *generate_array_random(int n);
int min(int *array, int n);
int max(int *array, int n);
int *sum_arrays(int *array1, int *array2, int n);


int main(){

    srand(time(NULL));

    int *array1 = generate_array_random(N);
    int *array2 = generate_array_random(N);

    printf("\nLista 1: ");

    for(int i = 0; i < N; i++){

        printf("%d, ", array1[i]);
    }
    printf("\n");

    printf("\nLista 2: ");

    for(int i = 0; i < N; i++){

        printf("%d, ", array2[i]);
    }
    printf("\n");

    printf("\nEl minimo de la Lista 1 es: %d\n", min(array1, N));
    printf("\nEl minimo de la Lista 2 es: %d\n", min(array2, N));

    printf("\nEl maximo de la Lista 1 es: %d\n", max(array1, N));
    printf("\nEl maximo de la Lista 2 es: %d\n", max(array2, N));

    int *sum = sum_arrays(array1, array2, N);

    printf("\nLista sumada: ");

    for (int i = 0; i < N; i++){

        printf("%d, ", sum[i]);
    }
    printf("\n");

    free(array1);
    free(array2);
    free(sum);

    return 0;
}

//Funcion que genera dos listas con numeros aleatorios

int *generate_array_random(int n){

    int* array = (int*)malloc(n * sizeof(int));

    if(array == NULL){

        printf("\nError: Memoria no asignada.");
        exit(1);
    }

    for(int i = 0; i < n; i++){

        array[i] = rand() % 201 - 100; //Numeros aleatorios entre -100 y 100
    }

    return array;
}

//Funcion que indica el valor minimo de cada lista

int min(int *array, int n){

    int mini = array[0];

    for(int i = 1; i < n; i++){

        if(array[i] < mini){

            mini = array[i];
        }
    }

    return mini;
}

//Funcion que indica el valor maximo de cada lista

int max(int *array, int n){

    int maxi = array[0];

    for(int i = 1; i < n; i++){

        if(array[i] > maxi){

            maxi = array[i];
        }
    }

    return maxi;
}

//Funcion que indica la suma de las dos listas

int *sum_arrays(int *array1, int *array2, int n){

    int *sum = (int*)malloc(n * sizeof(int));

    if(sum == NULL){

        printf("Error: Memoria no asignada.");
        exit(1);
    }

    for(int i = 0; i < n; i++){

        sum[i] = array1[i] + array2[i];
    }

    return sum;
}
