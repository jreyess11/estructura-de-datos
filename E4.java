import java.util.*;

//author Jose Reyes
public class E4 {

    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        Random rnd = new Random();
        System.out.print("Ingrese la cantidad de numeros: ");
        int N = scn.nextInt();

        int[] num = new int[N];

        for (int i=0; i<N; i++){
            int x = rnd.nextInt(100)+1;
            num[i]=x;
        }

        System.out.println("Sus numeros al azar son: " + Arrays.toString(num));
        System.out.println("El mayor numero generado es: " + Arrays.stream(num).max().getAsInt());
        System.out.print("El promedio de todos los numeros es: " + Arrays.stream(num).average().getAsDouble());
    }
}