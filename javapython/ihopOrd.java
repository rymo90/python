import java.util.*;

public class ihopOrd{
  // metod som lägger ihop ord
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int m = input.nextInt();
    String[] ord = new String [m];
    String namn;

    for (int i = 0;i < m;i++ ) {
      namn = input.next();
      ord[i] = namn;

    }
    for (String valu : ord) {
      System.out.println(valu);
    }
  }
}
