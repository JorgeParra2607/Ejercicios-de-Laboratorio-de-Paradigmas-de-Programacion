// Clase Circulo
public class Circulo {
    
    private String color;
    private double radio;

    public Circulo(String color, double radio) {
        this.color = color;
        this.radio = radio;
    }

    private double area() {
        return Math.PI * radio * radio;
    }

    private double perimetro() {
        return 2 * Math.PI * radio;
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
        return "Círculo [Color=" + color + ", Radio=" + radio + ", Área=" + getArea() + ", Perímetro=" + getPerimetro() + "]";
    }
}