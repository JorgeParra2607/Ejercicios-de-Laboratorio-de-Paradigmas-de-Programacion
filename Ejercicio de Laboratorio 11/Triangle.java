public class Triangle extends Figure {
    private double base;
    private double height;

    public Triangle(String color, double base, double height) {
        super(color);
        this.base = base;
        this.height = height;
    }

    @Override
    public double perimeter() {
        return 3 * base;
    }

    @Override
    public double area() {
        return 0.5 * base * height;
    }
}
