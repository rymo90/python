import java.util.Scanner;
import java.io.PrintStream;

import static java.lang.Math.sqrt;
import static java.lang.Math.pow;

public class akvariet{
  // my value
  private double xcordinat;
  private double ycordinat;
  private double zcordinat;
  // initierar my value
  public akvariet(double x, double y, double z){
    xcordinat = x;
    ycordinat = y;
    zcordinat = z;
  }
  public akvariet(){
  this (0,0,0);
  }
  // getter  value return a double
  public double getXcordinat(){
    return xcordinat;
  }
  public double getYcordinat(){
    return ycordinat;
  }
  public double getZcordinat(){
    return zcordinat;
  }
  // setter value
  public void setXcordinat(double xcordinat){
    this.xcordinat = xcordinat;
  }
  public void setYcordinat(double ycordinat){
    this.ycordinat = ycordinat;
  }
  public void setZcordinat(double zcordinat){
    this.zcordinat = zcordinat;
  }
  // method that make my qualqulation
  public double findTheDistence(akvariet p1, akvariet p2){
    double d = sqrt(pow(p1.getXcordinat()-p2.getXcordinat(), 2)+pow(p1.getYcordinat()-p2.getYcordinat(), 2)+pow(p1.getZcordinat()-p2.getZcordinat(), 2));
    return d;
  }

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int i = input.nextInt();
    double x1,y1,z1;
    double total = 0;
    // först punkten
    akvariet p1 = new akvariet();
    p1.setXcordinat(x1 = input.nextDouble());
    p1.setYcordinat(y1 = input.nextDouble());
    p1.setZcordinat(z1 = input.nextDouble());
    for (int j = 0;j<i-1;j++ ) {
      // andra punkten
      akvariet p2 = new akvariet();
      double x2,y2,z2;
      p2.setXcordinat(x2 = input.nextDouble());
      p2.setYcordinat(y2 = input.nextDouble());
      p2.setZcordinat(z2 = input.nextDouble());
      // hittar mellan två punkter
      double svar = p2.findTheDistence(p1, p2);

      // nu byter punkterna
      p1 = p2;
      total += svar;
    }
    System.out.format("%.02f%n", total);
  }

}
