#include <stdio.h>

int suma(int a, int b);
int resta(int a, int b);
int multiplicar(int a, int b);
int division(int a, int b);
float porcentaje(float cantidad, float porcentaje);
int cuadrado(int num);
int potencia(int base, int exponente);
int areaCuadrado(int lado);
float areaTriangulo(float base, float altura);
int modulo(int a, int b);

int main(){
    int opc, valor1, valor2;
    float cantidad, porc;

    do{
        printf("\n**MENU**\n");
        printf("Ingrese el numero correspondiente para realizar su respectiva accion: \n");
        printf("1. Suma de dos numeros\n");
        printf("2. Resta de dos numeros\n");
        printf("3. Multiplicacion de dos numeros\n");
        printf("4. Division de dos numeros\n");
        printf("5. Porcentaje de una cantidad\n");
        printf("6. Numero al cuadrado\n");
        printf("7. Numero a la n potencia\n");
        printf("8. Area de un cuadrado\n");
        printf("9. Area de un triangulo\n");
        printf("10. Modulo de dos numeros\n");
        printf("11. Salir\n\n");

        scanf("%d", &opc);

        switch(opc){

        case 1:
            printf("\nIngrese el primer numero a sumar: ");
            scanf("%d", &valor1);
            printf("Ingrese el segundo valor a sumar: ");
            scanf("%d", &valor2);
            printf("\nLa suma de los numeros es: %d", suma(valor1, valor2));
            printf("\n");
            break;

        case 2:
            printf("\nIngrese el primer numero a restar: ");
            scanf("%d", &valor1);
            printf("Ingrese el segundo valor a restar: ");
            scanf("%d", &valor2);
            printf("\nLa resta de los numeros es: %d", resta(valor1, valor2));
            printf("\n");
            break;

        case 3:
            printf("\nIngrese el primer numero a multiplicar: ");
            scanf("%d", &valor1);
            printf("Ingrese el segundo valor a multiplicar: ");
            scanf("%d", &valor2);
            printf("\nLa multiplicacion de los numeros es: %d", multiplicar(valor1, valor2));
            printf("\n");
            break;

        case 4:
            printf("\nIngrese el primer numero a dividir: ");
            scanf("%d", &valor1);
            printf("Ingrese el segundo valor a dividir: ");
            scanf("%d", &valor2);
            printf("\nLa division de los numeros es: %d", division(valor1, valor2));
            printf("\n");
            break;

        case 5:
            printf("\nIngrese la cantidad a calcular el porcentaje: ");
            scanf("%f", &cantidad);
            printf("Ingrese el porcentaje a calcular: ");
            scanf("%f", &porc);
            printf("\nEl porcentaje de %.2f es: %.2f", cantidad, porcentaje(cantidad, porc));
            printf("\n");
            break;

        case 6:
            printf("\nIngrese el numero para calcular su cuadrado: ");
            scanf("%d", &valor1);
            printf("\nEl cuadrado de %d es: %d", valor1, cuadrado(valor1));
            printf("\n");
            break;

        case 7:
            printf("\nIngrese el numero base: ");
            scanf("%d", &valor1);
            printf("Ingrese el exponente: ");
            scanf("%d", &valor2);
            printf("\n%d elevado a %d es: %d", valor1, valor2, potencia(valor1, valor2));
            printf("\n");
            break;

        case 8:
            printf("\nIngrese el valor del lado del cuadrado: ");
            scanf("%d", &valor1);
            printf("\nEl area del cuadrado es: %d", areaCuadrado(valor1));
            printf("\n");
            break;

        case 9:
            printf("\nIngrese el valor de la base del triangulo: ");
            scanf("%f", &cantidad);
            printf("Ingrese el valor de la altura del triangulo: ");
            scanf("%f", &porc);
            printf("\nEl area del triangulo es: %.2f", areaTriangulo(cantidad, porc));
            printf("\n");
            break;

        case 10:
            printf("\nIngrese el primer numero: ");
            scanf("%d", &valor1);
            printf("Ingrese el segundo numero: ");
            scanf("%d", &valor2);
            printf("\nEl modulo de %d y %d es: %d", valor1, valor2, modulo(valor1, valor2));
            printf("\n");
            break;
        }

    } while(opc != 11);

    return 0;
}

int suma(int a, int b){
    return a + b;
}

int resta(int a, int b){
    return a - b;
}

int multiplicar(int a, int b){
    return a * b;
}

int division(int a, int b){
    return a / b;
}

float porcentaje(float cantidad, float porcentaje){
    return cantidad * (porcentaje / 100.0);
}

int cuadrado(int num){
    return num * num;
}

int potencia(int base, int exponente){
    int resultado = 1;
    for (int i = 0; i < exponente; ++i) {
        resultado *= base;
    }
    return resultado;
}

int areaCuadrado(int lado){
    return lado * lado;
}

float areaTriangulo(float base, float altura){
    return (base * altura) / 2.0;
}

int modulo(int a, int b){
    return a % b;
}
