public class Persona{
    
    private String nombre; 
    private int edad; 
    private String direccion; 
    private String telefono; 
    private String email; 
    private String ocupacion; 
    private String nacionalidad; 
    
    public Persona(String nombre, int edad, String direccion, String telefono, String email, String ocupacion, String nacionalidad){
        
        this.nombre= nombre; 
        this.edad= edad;
        this.direccion= direccion; 
        this.telefono= telefono;
        this.email= email;
        this.ocupacion= ocupacion; 
        this.nacionalidad= nacionalidad;
    }
    
    public String getNombre(){
        
        return nombre;
    }

    public void setNombre(String nombre){
        
        this.nombre = nombre;
    }

    public int getEdad(){
        
        return edad;
    }

    public void setEdad(int edad){
        
        this.edad = edad;
    }

    public String getDireccion(){
        
        return direccion;
    }

    public void setDireccion(String direccion){
        
        this.direccion = direccion;
    }

    public String getTelefono(){
        
        return telefono;
    }

    public void setTelefono(String telefono){
        
        this.telefono = telefono;
    }

    public String getEmail(){
        
        return email;
    }

    public void setEmail(String email){
        
        this.email = email;
    }

    public String getOcupacion(){
        
        return ocupacion;
    }

    public void setOcupacion(String ocupacion){
        
        this.ocupacion = ocupacion;
    }

    public String getNacionalidad(){
        
        return nacionalidad;
    }

    public void setNacionalidad(String nacionalidad){
        
        this.nacionalidad = nacionalidad;
    }

    @Override
    public String toString(){
        
        return "Nombre: " + nombre + ", Edad: " + edad + ", Dirección: " + direccion + ", Teléfono: " + telefono + ", Email: " + email + ", Ocupación: " + ocupacion + ", Nacionalidad: " + nacionalidad;
    }

}