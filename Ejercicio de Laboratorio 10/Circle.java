class Circle extends Figure{
    private double radio;

    public Circle(String color, double radio){
        super(color);
        this.radio = radio;
    }

    @Override
    double perimetro(){
        return 2 * Math.PI * radio;
    }

    @Override
    double area(){
        return Math.PI * radio * radio;
    }
}
