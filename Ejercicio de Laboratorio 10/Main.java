public class Main {
    public static void main(String[] args){
        
        // Crear instancias de cada clase de figura
        Figure triangle = new Triangle("Rojo", 3, 4, 5);
        Figure circle = new Circle("Azul", 7);
        Figure rectangle = new Rectangle("Verde", 3, 5);
        Figure hexagon = new Hexagon("Amarillo", 7);

        Figure[] figuras = {triangle, circle, rectangle, hexagon};

        // Imprimir detalles de cada figura
        for (Figure figura : figuras) {
            System.out.println("Clase: " + figura.getClass().getSimpleName());
            System.out.println("Color: " + figura.getColor());
            System.out.println("Perimetro: " + figura.perimetro());
            System.out.println("Área: " + figura.area());
            System.out.println();
        }
    }
}
