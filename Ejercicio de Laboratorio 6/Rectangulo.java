// Clase Rectangulo
public class Rectangulo {
    
    private String color;
    private double base;
    private double altura;

    public Rectangulo(String color, double base, double altura) {
        this.color = color;
        this.base = base;
        this.altura = altura;
    }

    private double area() {
        return base * altura;
    }

    private double perimetro() {
        return 2 * (base + altura);
    }

    public String getColor() {
        return color;
    }

    public double getArea() {
        return area();
    }

    public double getPerimetro() {
        return perimetro();
    }

    @Override
    public String toString() {
        return "Rectángulo [Color=" + color + ", Base=" + base + ", Altura=" + altura + ", Área=" + getArea() + ", Perímetro=" + getPerimetro() + "]";
    }
}
