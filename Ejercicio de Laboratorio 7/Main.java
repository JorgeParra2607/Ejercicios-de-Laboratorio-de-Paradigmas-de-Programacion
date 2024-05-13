public class Main {
    public static void main(String[] args){
        
        // Crear arreglo de 10 objetos Punto3D
        Punto3D[] puntos = new Punto3D[10];
        
        for (int i = 0; i < 10; i++){
            puntos[i] = new Punto3D(i, i * 2, i * 3);
        }

        // Calcular la distancia entre todos los objetos y determinar la menor distancia
        double menorDistancia = Double.POSITIVE_INFINITY;
        
        for (int i = 0; i < puntos.length; i++){
            
            for (int j = i + 1; j < puntos.length; j++){
                
                double distanciaActual = puntos[i].distancia(puntos[j]);
                System.out.println("Distancia entre puntos " + i + " y " + j + ": " + distanciaActual);
                
                if (distanciaActual < menorDistancia){
                    menorDistancia = distanciaActual;
                }
            }
        }

        System.out.println("\nLa menor distancia es: " + menorDistancia);
    }
}