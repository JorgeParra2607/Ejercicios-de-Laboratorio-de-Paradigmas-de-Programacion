import java.io.IOException;

public class PruebaLecturaNumeros{
    public static void main(String[] args){
        try{
            LecturaNumeros lector = new LecturaNumeros();
            
            System.out.println("Introduce 2 números enteros:");
            int num1 = lector.readInt();
            int num2 = lector.readInt();
            
            System.out.println("\nIntroduce un número entero (en forma de Integer):");
            Integer numInteger = lector.readInteger();
            
            System.out.println("\nIntroduce un número decimal:");
            double numDouble = lector.readDouble();
            
            System.out.println("\nIntroduce un número decimal (en forma de Double):");
            double numDouble2 = lector.readDouble();
            
            System.out.println("\nNúmeros introducidos:");
            System.out.println("Entero 1: " + num1);
            System.out.println("Entero 2: " + num2);
            System.out.println("Integer: " + numInteger);
            System.out.println("Double: " + numDouble);
            System.out.println("Double 2: " + numDouble2);
            
            lector.close(); // Cerrar el lector al finalizar
            
        } catch (IOException e){
            System.err.println("Error de lectura: " + e.getMessage());
        }
    }
}
