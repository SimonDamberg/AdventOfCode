import java.io.*;
import java.util.*;

public class Day6 {

    public static void main(String[] args) throws FileNotFoundException{
      File file = new File("input.txt");
      Scanner scanner = new Scanner(file);
      ArrayList<List<String>> rows = new ArrayList<List<String>>();
      List<String> currentBatch = new ArrayList<String>();
      String inputString = "";
      while(scanner.hasNextLine()){
        inputString = scanner.nextLine();
        if(inputString.length() == 0){
          rows.add(currentBatch);
          currentBatch = new ArrayList<String>();
        }else{
          currentBatch.add(inputString);
        }
      }
      rows.add(currentBatch); //Last row
      int part1Sum = 0;
      int part2Sum = 0;
      for(List<String> batch: rows){
        HashMap<Character, Integer> hashMap = new HashMap<Character, Integer>();
        for(String s : batch){
          for(int i = 0; i < s.length(); i++){
            if(hashMap.containsKey(s.charAt(i))){
              hashMap.put(s.charAt(i), hashMap.get(s.charAt(i))+1);
            }else{
              hashMap.put(s.charAt(i), 1);
            }
          }
        }
        part1Sum += hashMap.size();
        Collection<Integer> values = hashMap.values();
        for(Integer i: values){
          if(i == batch.size()){
            part2Sum += 1;
          }
        }
      }
      System.out.println("Part 1: " + part1Sum);
      System.out.println("Part 2: " + part2Sum);
    }
}
