import java.io.*;
import java.util.*;

public class Day12 {

    private static int facing;
    private static int posNorthSouthP1;
    private static int posWestEastP1;
    private static int posNorthSouthP2;
    private static int posWestEastP2;
    private static int waypointNorthSouth;
    private static int waypointWestEast;

    public static void main(String[] args) throws FileNotFoundException{
      posNorthSouthP1 = 0;
      posWestEastP1 = 0;
      facing = 90;
      posNorthSouthP2 = 0;
      posWestEastP2 = 0;
      waypointNorthSouth = 1;
      waypointWestEast = 10;
      File file = new File("input.txt");
      Scanner scanner = new Scanner(file);
      String InputString = "";
      while(scanner.hasNextLine()){
        InputString = scanner.nextLine();
        changePositionPart1(InputString);
        changePositionPart2(InputString);
      }
      int sumPart1 = Math.abs(posNorthSouthP1) + Math.abs(posWestEastP1);
      int sumPart2 = Math.abs(posNorthSouthP2) + Math.abs(posWestEastP2);
      System.out.println("Part 1: " + sumPart1);
      System.out.println("Part 2: " + sumPart2);
    }

    public static void changePositionPart2(String command){
      char action = command.charAt(0);
      int value = Integer.parseInt(command.substring(1));
      switch (action) {
        case 'N':
          waypointNorthSouth += value;
          break;
        case 'S':
          waypointNorthSouth -= value;
          break;
        case 'E':
          waypointWestEast += value;
          break;
        case 'W':
          waypointWestEast -= value;
          break;
        case 'L':
          value = value % 360;
          switch (value) {
            case 0:
              break;
            case 90:
              int currWestEast = waypointWestEast;
              waypointWestEast = -waypointNorthSouth;
              waypointNorthSouth = currWestEast;
              break;
            case 180:
              waypointWestEast = -waypointWestEast;
              waypointNorthSouth = -waypointNorthSouth;
              break;
            case 270:
              int currNorthSouth = waypointNorthSouth;
              waypointNorthSouth = -waypointWestEast;
              waypointWestEast = currNorthSouth;
              break;
            default:
              System.out.println("FAIL " + value);
              break;
          }
          break;
        case 'R':
          value = value % 360;
          switch (value) {
            case 0:
              break;
            case 90:
              int currNorthSouth = waypointNorthSouth;
              waypointNorthSouth = -waypointWestEast;
              waypointWestEast = currNorthSouth;
              break;
            case 180:
              waypointWestEast = -waypointWestEast;
              waypointNorthSouth = -waypointNorthSouth;
              break;
            case 270:
              int currWestEast = waypointWestEast;
              waypointWestEast = -waypointNorthSouth;
              waypointNorthSouth = currWestEast;
              break;
            default:
              System.out.println("FAIL " + value);
              break;
          }
          break;
        case 'F':
          posNorthSouthP2 += waypointNorthSouth*value;
          posWestEastP2 += waypointWestEast*value;
          break;
        default:
          System.out.println("FAIL");
          break;
      }
    }

    public static void changePositionPart1(String command){
      // Modulo in java didn't act as expected, this is a work around.
      if(facing < 0){
        facing = 360 + facing;
      }
      facing = facing % 360;
      char action = command.charAt(0);
      int value = Integer.parseInt(command.substring(1));
      switch (action) {
        case 'N':
          posNorthSouthP1 += value;
          break;
        case 'S':
          posNorthSouthP1 -= value;
          break;
        case 'E':
          posWestEastP1 += value;
          break;
        case 'W':
          posWestEastP1 -= value;
          break;
        case 'L':
          facing -= value;
          break;
        case 'R':
          facing += value;
          break;
        case 'F':
          switch (facing) {
            case 0:
              changePositionPart1("N" + value);
              break;
            case 90:
              changePositionPart1("E" + value);
              break;
            case 180:
              changePositionPart1("S" + value);
              break;
            case 270:
              changePositionPart1("W" + value);
              break;
            default:
              break;
          }
          break;
        default:
          System.out.println("FAIL");
          break;
      }
    }
}
