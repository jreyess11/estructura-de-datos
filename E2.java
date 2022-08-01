import java.util.Scanner;
import java.util.Arrays;

//author Jose Reyes
public class E2 {
    public static int count(int[] a, int b){
        int cont=0;
        for (int i=0;i<a.length;i++) {
            if (a[i] == b) {
                cont += 1;
            }
        }
        return cont;
    }

    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int r=0;

        System.out.print("Ingrese la cantidad de numeros a leer: ");
        int cant=scn.nextInt();

        int[] ln = new int[cant];

        while (r<cant){
            System.out.printf("Ingrese el numero %d: ", r+1);
            int num = scn.nextInt();
            ln[r]=num;
            r+=1;
        }
        System.out.printf("El mayor numero leido es %d y se repite %d veces.", Arrays.stream(ln).max().getAsInt(),count(ln, Arrays.stream(ln).max().getAsInt()));
    }
}