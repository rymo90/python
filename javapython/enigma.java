import java.util.*;
import java.lang.*;


public class enigma{

  public static void indexOf(String kryptext, String klartext){
    char[] krypchar = kryptext.toCharArray();
    char[] klarchar = klartext.toCharArray();
    int diff = krypchar.length - klarchar.length;
    boolean no_found_solo = true;
    for (int i = 0;i <=diff ;i++ ) {
      boolean fond_solo = true;
      for (int j = 0;j < klarchar.length ;j++ ) {
        if(klarchar[j]==krypchar[j+i]){
          fond_solo = false;
          break;
        }
      }
      if(fond_solo){
        no_found_solo = false;
        System.out.print(i+1);
        System.out.print(" ");
      }
    }
    if (no_found_solo) {
      System.out.print(-1);
    }
  }


  public static void main(String[] args) {
    Scanner input = new Scanner (System.in);
    String kryptext = input.next();
    String klartext = input.next();
    indexOf(kryptext,klartext);
    }

}
