public class Hexagon extends Figure {
    private double side;

    public Hexagon(String color, double side) {
        super(color);
        this.side = side;
    }

    @Override
    public double perimeter() {
        return 6 * side;
    }

    @Override
    public double area() {
        return (3 * Math.sqrt(3) / 2) * Math.pow(side, 2);
    }
}
