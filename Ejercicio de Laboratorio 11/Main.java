public class Main {
    public static void main(String[] args) {
        // Crear instancias de las figuras
        Triangle triangulo = new Triangle("Rojo", 5, 4);
        Circle circulo = new Circle("Azul", 3);
        Rectangle rectangulo = new Rectangle("Verde", 6, 8);
        Hexagon hexagono = new Hexagon("Amarillo", 7);

        // Mostrar características de cada figura
        System.out.println("Triángulo - Color: " + triangulo.getColor() +
                ", Perímetro: " + triangulo.perimeter() +
                ", Área: " + triangulo.area());

        System.out.println("Círculo - Color: " + circulo.getColor() +
                ", Perímetro: " + circulo.perimeter() +
                ", Área: " + circulo.area());

        System.out.println("Rectángulo - Color: " + rectangulo.getColor() +
                ", Perímetro: " + rectangulo.perimeter() +
                ", Área: " + rectangulo.area());

        System.out.println("Hexágono - Color: " + hexagono.getColor() +
                ", Perímetro: " + hexagono.perimeter() +
                ", Área: " + hexagono.area());
    }
}
