import java.util.Scanner;

//author Jose Reyes
public class E1 {

    public static void main(String[] args) {
        int cant, suma = 0, pos = 0, neg = 0;
        Scanner scn = new Scanner(System.in);

        System.out.print("Ingrese la cantidad de numeros a leer: ");
        cant=scn.nextInt();

        for (int i=0; i<cant; i++){
            System.out.printf("Ingrese el numero %d: ", i+1);
            int num=scn.nextInt();
            suma+=num;
            if (num>0){
                pos += num;
            }
            if (num<0){
                neg += num;
            }

        }
        System.out.printf("La suma total es %d, la suma de todos los positivos es %d y la de todos los negativos es %d.", suma, pos, neg);
    }
}