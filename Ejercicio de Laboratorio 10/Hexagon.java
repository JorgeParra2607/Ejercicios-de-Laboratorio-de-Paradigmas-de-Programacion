class Hexagon extends Figure{
    private double lado;

    public Hexagon(String color, double lado){
        super(color);
        this.lado = lado;
    }

    @Override
    double perimetro(){
        return 6 * lado;
    }

    @Override
    double area(){
        return (3 * Math.sqrt(3) * lado * lado) / 2;
    }
}
