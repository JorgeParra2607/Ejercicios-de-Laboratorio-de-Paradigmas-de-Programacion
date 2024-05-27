abstract class Figure{
    protected String color;

    public Figure(String color){
        this.color = color;
    }

    public String getColor(){
        return color;
    }

    abstract double perimetro();
    abstract double area();
}

