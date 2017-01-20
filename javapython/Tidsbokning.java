import java.util.*;
class MeetingTime implements Comparable<MeetingTime>{
  private String veckordagar;
  private int indexVote;

  public MeetingTime(String dag, int votes){
    veckordagar = dag;
    indexVote = votes;
  }
  public String getDag(){
    return veckordagar;
  }
  public void setVeckorDagar(String veckordagar){
    this.veckordagar = veckordagar;
  }
  public int getVote(){
    return indexVote;
  }
  public void setIndexVote(int indexVote){
    this.indexVote= indexVote;
  }
  public String toString(){
    return getDag() + " "+ getVote();
  }
  public int compareTo(MeetingTime other){
    if (getVote()== other.getVote()) {
      return 0;
    }else if (getVote() > other.getVote()){
      return -1;
    }else{
      return 1;
    }
  }
}
public class Tidsbokning{

  public static int[][] bokning(int antal_pers,  Scanner input){
    int[][] boka = new int[antal_pers][];
    String temp;
    for (int i = 0;i < antal_pers ;i++ ) {
      temp = input.nextLine();
      String[] noFirst = temp.split(" ");
      noFirst = Arrays.copyOfRange(noFirst,1, noFirst.length);
      boka[i] = new int[noFirst.length];
      for (int j = 0;j<noFirst.length ;j++ ) {
        boka[i][j] = Integer.parseInt(noFirst[j]);
      }
    }
    return boka;
  }
  public static String[] veckor(int antal_mote , Scanner input){
    String[] vecka = new String[antal_mote];
    for (int i = 0; i < antal_mote ;i++ ){
      vecka[i] = input.nextLine();
    }
    return vecka;
  }
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int antal_mote, antal_pers;
    antal_mote = input.nextInt();
    antal_pers = input.nextInt();
    input.nextLine();
    String[] svar = veckor(antal_mote, input);
    int[][] svar2 = bokning(antal_pers,input);
    int lend = svar.length;
    int[]counter = new int[lend];
    for (int i = 0;i < lend ;i++ ) {
      int vote = 0;
      for (int j = 0;j < svar2.length;j++ ) {
        for (int m= 0;m < svar2[j].length ;m++ ) {
          if (svar2[j][m]==i) {
            vote++;
          }
        }
      }
      counter[i] = vote;
    }
    List <MeetingTime> lista = new ArrayList<MeetingTime>();
    for (int i=0;i<lend;i++ ) {
      MeetingTime doodle = new MeetingTime(svar[i],counter[i]);
      lista.add(doodle);
    }
    Collections.sort(lista);
    Iterator itr = lista.iterator();
    while(itr.hasNext()){
      Object element = itr.next();
      System.out.println(element );
        }
  }


}
