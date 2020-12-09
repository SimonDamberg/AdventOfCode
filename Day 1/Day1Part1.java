import java.io.*;
import java.util.*;

public class Day1Part1 {

    public static void main(String[] args) throws FileNotFoundException{
      int result = 0;
      File file = new File("day1.txt");
      Scanner scanner = new Scanner(file);
      String InputString = "";
      ArrayList<Integer> allNumbers = new ArrayList<Integer>();
      while(scanner.hasNextInt()){
        allNumbers.add(scanner.nextInt());
      }
      for(int i : allNumbers){
        for(int j : allNumbers){
          if(i+j == 2020){
            result = i*j;
            break;
          }
        }
      }
      System.out.println("Result: " + result);
    }
}
