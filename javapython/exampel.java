import java.util.*;
import java.lang.*;
import java.io.*;

public class exampel{
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    String a = input.next();
    String b = input.next();
    int counter = 0;
    char[] krypchar = a.toCharArray();
    char[] klarchar = b.toCharArray();
    int diff = krypchar.length - klarchar.length;
    int resultat[] = new int[diff+1];
    for (int i = 1; i <= diff ;i++ ) {
      for (int j = 0; j < klarchar.length ;j++ ) {
        if (klarchar[j]!=krypchar[j]) {
          resultat[i]=
        }else{
          counter =0;
        }
        

      }
      resultat[i]= counter;

      }
      for (int c :resultat ) {
        System.out.println(c);

      }
    }




}
