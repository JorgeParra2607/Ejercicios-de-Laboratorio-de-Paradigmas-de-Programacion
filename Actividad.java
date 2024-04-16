public class Actividad {
    
    public static void main(String[] args){
        
        Persona p1 = new Persona("Jorge", 26, "Estado de Mexico, Ixtapaluca", "123456789", "jorge26@ipn.mx", "Ingeniero", "Mexicana");
        System.out.println("Nombre: " + p1.getNombre());
        System.out.println("Edad: " + p1.getEdad());
        System.out.println("Dirección: " + p1.getDireccion());
        System.out.println("Teléfono: " + p1.getTelefono());
        System.out.println("Email: " + p1.getEmail());
        System.out.println("Ocupación: " + p1.getOcupacion());
        System.out.println("Nacionalidad: " + p1.getNacionalidad());
        
    }
    
}