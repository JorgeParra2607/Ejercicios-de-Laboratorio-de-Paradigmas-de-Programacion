public class Main {
    
    public static void main(String[] args) {

        // Circulo
        Circulo circulo = new Circulo("Rojo", 7.0);
        System.out.println("Círculo:");
        System.out.println("Color: " + circulo.getColor());
        System.out.println("Área= " + circulo.getArea());
        System.out.println("Perímetro= " + circulo.getPerimetro());
        
        // Rectangulo
        Rectangulo rectangulo = new Rectangulo("Azul", 5.0, 7.0);
        System.out.println("\nRectángulo:");
        System.out.println("Color: " + rectangulo.getColor());
        System.out.println("Área= " + rectangulo.getArea());
        System.out.println("Perímetro= " + rectangulo.getPerimetro());

        // Cuadrado
        Cuadrado cuadrado = new Cuadrado("Verde", 5.0);
        System.out.println("\nCuadrado:");
        System.out.println("Color: " + cuadrado.getColor());
        System.out.println("Área= " + cuadrado.getArea());
        System.out.println("Perímetro= " + cuadrado.getPerimetro());

        // Triangulo
        Triangulo triangulo = new Triangulo("Amarillo", 3.0, 4.0, 5.0);
        System.out.println("\nTriángulo:");
        System.out.println("Color: " + triangulo.getColor());
        System.out.println("Área= " + triangulo.getArea());
        System.out.println("Perímetro= " + triangulo.getPerimetro());

    }
}
