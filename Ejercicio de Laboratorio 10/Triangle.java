class Triangle extends Figure{
    private double lado1, lado2, lado3;

    public Triangle(String color, double lado1, double lado2, double lado3){
        super(color);
        this.lado1 = lado1;
        this.lado2 = lado2;
        this.lado3 = lado3;
    }

    @Override
    double perimetro(){
        return lado1 + lado2 + lado3;
    }

    @Override
    double area(){
        double s = perimetro() / 2;
        return Math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3));
    }
}
