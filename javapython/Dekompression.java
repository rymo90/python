import java.util.*;
import java.io.*;
import java.lang.*;
public class Dekompression{
  public static String decompress(Queue<Character>q){
    StringBuilder temp = new StringBuilder();
    StringBuilder konv = new StringBuilder();
    String result="";
    String sub="";
    String repeated="";
    int num=1;
    try {
      while(Character.isLetterOrDigit(q.peek())) {
        if (Character.isDigit(q.peek())) {
          konv.append(q.poll());
          num = Integer.parseInt(konv.toString());
        }else{
          konv.delete(0,konv.length());
          if (num==1 && konv.length()==0) {
            num = 1;
          }
          repeated = new String (new char[num]).replace("\0",String.valueOf(q.poll()));
          sub += repeated;
          num = 1;
        }
      }
      if(q.peek()==')') {
        q.poll();
        return sub;
      }
      if(q.peek()=='('){
        q.poll();
        repeated = new String(new char[num]).replace("\0",decompress(q));
        sub = sub + repeated;
      }
      if(q.isEmpty()){
        return sub;
      }else{
        sub = sub+ decompress(q);
      }
    }catch (NullPointerException e) {

    }finally{

    }
    return sub;
  }
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    String s = input.next();
    Queue<Character> q = new LinkedList<Character>();
    char[] chr = s.toCharArray();
    for (char y : chr) {
      q.offer(y);
    }
    System.out.println(decompress(q));
  }
}
