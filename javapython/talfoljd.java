import java.util.*;

public class talfoljd{

  public static int jemnUdda(int i, int r){
    while(i != 1){
      if((i%2)==0){
        i=i/2;
        r++;
      }
      else{
        i=(i*3)+1;
        r++;
      }
    }
    return r;
  }

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int x = input.nextInt();
    int y = input.nextInt();
    int r = 0;
    while (x<=y) {
      int i=x;
      int a = jemnUdda(i, r);
      System.out.println(a);
      x++;
    }
  }
}
