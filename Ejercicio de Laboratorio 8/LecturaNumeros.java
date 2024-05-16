import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;

public class LecturaNumeros extends BufferedReader{
    
    public LecturaNumeros(){
        super(new InputStreamReader(System.in));
    }
    
    public LecturaNumeros(Reader r){
        super(r);
    }
    
    public int readInt() throws IOException{
        String input = super.readLine();
        return Integer.parseInt(input);
    }
    
    public int readInt(String mensaje) throws IOException{
        System.out.print(mensaje);
        return readInt();
    }

    public Integer readInteger() throws IOException{
        return readInt();
    }
    
    public double readDouble() throws IOException{
        String input = super.readLine();
        return Double.parseDouble(input);
    }
    
    public double readDouble(String mensaje) throws IOException{
        System.out.print(mensaje);
        return readDouble();
    }
}
