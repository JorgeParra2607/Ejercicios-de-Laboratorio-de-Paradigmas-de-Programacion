import java.lang.Math;

class Punto3D {
    private double x;
    private double y;
    private double z;

    // Constructores sobrecargados
    public Punto3D(){
        this(0, 0, 0);
    }

    public Punto3D(double x, double y, double z){
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public Punto3D(Punto3D otroPunto){
        this.x = otroPunto.getX();
        this.y = otroPunto.getY();
        this.z = otroPunto.getZ();
    }

    // Métodos set
    public void setX(double x){
        this.x = x;
    }

    public void setY(double y){
        this.y = y;
    }

    public void setZ(double z){
        this.z = z;
    }

    // Métodos get
    public double getX(){
        return this.x;
    }

    public double getY(){
        return this.y;
    }

    public double getZ(){
        return this.z;
    }

    // Método distancia euclidiana
    public double distancia(Punto3D otroPunto){
        double distanciaX = this.x - otroPunto.getX();
        double distanciaY = this.y - otroPunto.getY();
        double distanciaZ = this.z - otroPunto.getZ();
        return Math.sqrt(distanciaX * distanciaX + distanciaY * distanciaY + distanciaZ * distanciaZ);
    }
}