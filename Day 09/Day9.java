import java.io.*;
import java.util.*;

public class Day9 {

    public static boolean validNum(ArrayList<Integer> preamble, int num)
    {
      for(int i : preamble)
      {
        for(int j : preamble)
        {
          if(i+j == num)
          {
            return true;
          }
        }
      }
      return false;
    }

    public static void main(String[] args) throws FileNotFoundException{
      File file = new File("input.txt");
      Scanner scanner = new Scanner(file);
      String InputString = "";
      ArrayList<Integer> allNumbers = new ArrayList<Integer>();
      while(scanner.hasNextInt()){
        allNumbers.add(scanner.nextInt());
      }
      ArrayList<Integer> preamble = new ArrayList<Integer>();
      for(int i = 0; i<25; i++)
      {
        preamble.add(allNumbers.get(i));
      }
      int part1 = 0;
      for(int i = 25; i<allNumbers.size(); i++)
      {
        if(validNum(preamble, allNumbers.get(i)) != true)
        {
          part1 = allNumbers.get(i);
          break;
        }
        preamble.remove(0);
        preamble.add(allNumbers.get(i));
      }
      boolean foundSum = false;
      ArrayList<Integer> countinousNumbers = new ArrayList<Integer>();
      for(int i = 0; i < allNumbers.size(); i++)
      {
        long sum = 0;
        int j = i;
        boolean notLarger = true;
        while(notLarger)
        {
          countinousNumbers.add(allNumbers.get(j));
          sum += allNumbers.get(j);
          if(sum < part1)
          {
            j++;
          } else if (sum == part1) {
            foundSum = true;
            break;
          } else {
            notLarger = false;
          }
        }
        if(foundSum == true)
        {
          break;
        }
        countinousNumbers.clear();
      }
      int part2 = Collections.min(countinousNumbers) + Collections.max(countinousNumbers);
      System.out.println("Part 1: " + part1);
      System.out.println("Part 2: " + part2);

    }
}
