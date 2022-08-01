import java.util.*;

public class E3 {
    public static boolean primo(int n){
        int m=n/2;
        for(int i=2; i<=m; i++){
            if (n%i==0){
                return false;
            }
        } return true;
    }

    public static void main(String[] args) {
        boolean loop = true;
        while (loop) {
            try {
                int cont = 0, x = 1;
                Scanner scn = new Scanner(System.in);
                System.out.print("Ingrese la cantidad de numeros primos: ");
                int N = scn.nextInt();
                List<Integer> primos = new LinkedList<>();

                while (cont < N) {
                    x += 1;
                    if (primo(x)) {
                        primos.add(x);
                        cont += 1;
                    }
                }
                StringJoiner joiner = new StringJoiner(", ", "", ".");
                primos.forEach(item -> joiner.add(Objects.toString(item)));
                System.out.println(joiner);
                loop = false;

            } catch (Exception e) {
                System.out.println("Ingrese un numero entero valido.");
            }
        }
    }
}
