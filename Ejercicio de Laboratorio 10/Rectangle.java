class Rectangle extends Figure{
    private double ancho, alto;

    public Rectangle(String color, double ancho, double alto){
        super(color);
        this.ancho = ancho;
        this.alto = alto;
    }

    @Override
    double perimetro(){
        return 2 * (ancho + alto);
    }

    @Override
    double area(){
        return ancho * alto;
    }
}
