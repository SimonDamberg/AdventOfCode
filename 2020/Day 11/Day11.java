import java.io.*;
import java.util.*;

public class Day11 {

    public static void main(String[] args) throws FileNotFoundException{
      File file = new File("input.txt");
      Scanner scanner = new Scanner(file);
      String InputString = "";
      // File for part 1
      ArrayList<ArrayList<Character>> seats = new ArrayList<ArrayList<Character>>();
      ArrayList<ArrayList<Character>> seats2 = new ArrayList<ArrayList<Character>>();
      while(scanner.hasNextLine()){
        InputString = scanner.nextLine();
        ArrayList<Character> row = new ArrayList<Character>();
        for(int i = 0; i < InputString.length(); i++){
          row.add(InputString.charAt(i));
        }
        seats.add(row);
        seats2.add(row);
      }
      while(! seats.equals(seats = updateSeatsPart1(seats))){}
      while(! seats2.equals(seats2 = updateSeatsPart2(seats2))){}
      int occupiedSeatsPart1 = 0;
      int occupiedSeatsPart2 = 0;
      for(int i = 0; i<seats.size(); i++){
        for(int j = 0; j<seats.get(i).size(); j++){
          if(seats.get(i).get(j).equals('#')){
              occupiedSeatsPart1++;
          }
          if(seats2.get(i).get(j).equals('#')){
              occupiedSeatsPart2++;
          }
        }
      }
      System.out.println("Part 1:" + occupiedSeatsPart1);
      System.out.println("Part 2:" + occupiedSeatsPart2);
    }

    public static Boolean checkOccupied(ArrayList<Character> row, int seatNum){
      if(row.get(seatNum).equals('#')){
        return true;
      } else {
        return false;
      }
    }

    public static int checkAdjacent(ArrayList<Character> row, int seatNum){
      int adjacentOccupied = 0;
      if(seatNum == 0){
        for(int i = seatNum; i < seatNum+2; i++){
          if(checkOccupied(row, i)){
            adjacentOccupied++;
          }
        }
      } else if(seatNum == row.size()-1) {
        for(int i = seatNum-1; i < seatNum+1; i++){
          if(checkOccupied(row, i)){
            adjacentOccupied++;
          }
        }
      }
      else {
        for(int i = seatNum-1; i < seatNum+2; i++){
          if(checkOccupied(row, i)){
            adjacentOccupied++;
          }
        }
      }
      return adjacentOccupied;
    }

    public static int checkSeat(ArrayList<ArrayList<Character>> seats, int rowNum, int seatNum){
      int totOccupied = 0;
      if(rowNum == 0){
        totOccupied += checkAdjacent(seats.get(rowNum), seatNum);
        totOccupied += checkAdjacent(seats.get(rowNum+1), seatNum);
      } else if(rowNum == seats.size()-1){
        totOccupied += checkAdjacent(seats.get(rowNum), seatNum);
        totOccupied += checkAdjacent(seats.get(rowNum-1), seatNum);
      } else {
        totOccupied += checkAdjacent(seats.get(rowNum+1), seatNum);
        totOccupied += checkAdjacent(seats.get(rowNum), seatNum);
        totOccupied += checkAdjacent(seats.get(rowNum-1), seatNum);
      }
      return totOccupied;
    }

    public static ArrayList<ArrayList<Character>> updateSeatsPart1(ArrayList<ArrayList<Character>> seats){
      ArrayList<ArrayList<Character>> newState = new ArrayList<ArrayList<Character>>();
      for(int i = 0; i<seats.size(); i++){
        newState.add(new ArrayList<Character>());
        for(int j = 0; j<seats.get(i).size(); j++){
          newState.get(i).add(seats.get(i).get(j));
          int totOccupied = checkSeat(seats, i, j);
          if(seats.get(i).get(j).equals('L')){ // Seat is free
            if(totOccupied == 0){
              newState.get(i).set(j, '#');
            }
          } else if(seats.get(i).get(j).equals('#')) { // Seat is occupied
            if(totOccupied-1 >= 4){ //Removes current seat from result
              newState.get(i).set(j, 'L');
            }
          }
        }
      }
      return newState;
    }

    public static ArrayList<ArrayList<Character>> updateSeatsPart2(ArrayList<ArrayList<Character>> seats){
      ArrayList<ArrayList<Character>> newState = new ArrayList<ArrayList<Character>>();
      for(int i = 0; i<seats.size(); i++){
        newState.add(new ArrayList<Character>());
        for(int j = 0; j<seats.get(i).size(); j++){
          newState.get(i).add(seats.get(i).get(j));
          int totOccupied = 0;
          // Check horizontally
          List<Character> firstHalf = seats.get(i).subList(0, j);
          ArrayList<Character> reversedHalf = new ArrayList<Character>();
          for(int k = firstHalf.size()-1; k >= 0; k--){
            reversedHalf.add(firstHalf.get(k));
          }
          List<Character> secondHalf = seats.get(i).subList(j+1, seats.get(i).size());
          totOccupied += (visableOccupiedSeats(reversedHalf) + visableOccupiedSeats(secondHalf));

          // Check vertically
          firstHalf = new ArrayList<Character>();
          secondHalf = new ArrayList<Character>();
          for(int k = i-1; k >=0; k--){
            firstHalf.add(seats.get(k).get(j));
          }
          for(int k = i+1; k<seats.size(); k++){
            secondHalf.add(seats.get(k).get(j));
          }
          totOccupied += (visableOccupiedSeats(firstHalf) + visableOccupiedSeats(secondHalf));

          // Check upper diagonals
          firstHalf = new ArrayList<Character>();
          secondHalf = new ArrayList<Character>();
          int left = j-1;
          int right = j+1;
          for(int k = i-1; k >= 0; k--){
            if(left >= 0){
              firstHalf.add(seats.get(k).get(left));
            }
            if(right < seats.get(k).size()){
              secondHalf.add(seats.get(k).get(right));
            }
            left--;
            right++;
          }
          totOccupied += (visableOccupiedSeats(firstHalf) + visableOccupiedSeats(secondHalf));

          // Check lower diagonals
          firstHalf = new ArrayList<Character>();
          secondHalf = new ArrayList<Character>();
          left = j-1;
          right = j+1;
          for(int k = i+1; k < seats.size(); k++){
            if(left >= 0){
              firstHalf.add(seats.get(k).get(left));
            }
            if(right < seats.get(k).size()){
              secondHalf.add(seats.get(k).get(right));
            }
            left--;
            right++;
          }
          totOccupied += (visableOccupiedSeats(firstHalf) + visableOccupiedSeats(secondHalf));
          // if(seats.get(i).get(j).equals('#') || seats.get(i).get(j).equals('L')){
          //   System.out.println(totOccupied);
          // }
          // if(seats.get(i).get(j).equals('#')){
          //   System.out.println("#######");
          // }
          if(seats.get(i).get(j).equals('L') && totOccupied == 0){ // Seat is free
            newState.get(i).set(j, '#');
          } else if(seats.get(i).get(j).equals('#') && totOccupied >= 5) { // Seat is occupied
            newState.get(i).set(j, 'L');
        }
        }
      }
      return newState;

    }

    public static int visableOccupiedSeats(List<Character> row){
      for(int i = 0; i<row.size(); i++){
        if(row.get(i).equals('#')){
          return 1;
        } else if(row.get(i).equals('L')){
          return 0;
        }
      }
      return 0;
    }

}
