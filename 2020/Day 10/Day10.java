import java.io.*;
import java.util.*;

public class Day10 {

    public static void main(String[] args) throws FileNotFoundException{
      File file = new File("input.txt");
      Scanner scanner = new Scanner(file);
      String InputString = "";
      ArrayList<Integer> allJoltages = new ArrayList<Integer>();
      while(scanner.hasNextInt()){
        allJoltages.add(scanner.nextInt());
      }
      Collections.sort(allJoltages);
      System.out.println(allJoltages);
      int prevJolt = 0;
      int no1Diff = 0;
      int no3Diff = 0;
      for(int adapterRating : allJoltages)
      {
        if(adapterRating-prevJolt == 1)
        {
          no1Diff++;
        } else if(adapterRating-prevJolt == 3)
        {
          no3Diff++;
        }
        prevJolt = adapterRating;
      }
      no3Diff++;
      System.out.println("Part 1: " + (no1Diff*no3Diff));
    }
}
