import java.io.*;
import java.util.*;

public class Day2Part1 {

    public static void main(String[] args) throws FileNotFoundException{
      int noValidPasswords = 0;
      File file = new File("day2.txt");
      Scanner scanner = new Scanner(file);
      String InputString = "";
      while(scanner.hasNextLine()){
        InputString = scanner.nextLine();
        int lowerBound = Integer.parseInt(InputString.split("\\-", 0)[0]);
        int upperBound = Integer.parseInt(InputString.split("\\-", 0)[1].split(" ", 0)[0]);
        char letter = InputString.split(" ", 0)[1].charAt(0);
        String password = InputString.split(" ", 0)[2];
        int charOccurences = 0;
        for(int i = 0; i < password.length(); i++){
          if(password.charAt(i) == letter){
            charOccurences ++;
          }
        }
        if(charOccurences >= lowerBound && charOccurences <= upperBound){
          noValidPasswords++;
        }
      }
      System.out.println("Counter: " + noValidPasswords);
    }
}
