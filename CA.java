package Phys2010_Final;
import java.util.Random;

public class CrystalGrowthCA {
    public static final int GRID_SIZE = 100;
    public static final int NUM_PARTICLES = 1000;
    public static final int EMPTY = 0;
    public static final int CRYSTAL = 1;
    public static final int PARTICLE = 2;

    public static void simulateCrystalGrowth(int[][] grid) {
        grid[GRID_SIZE / 2][GRID_SIZE / 2] = CRYSTAL;
        Random rand = new Random();
        for (int i = 0; i < NUM_PARTICLES; i++) {
            int x = rand.nextInt(GRID_SIZE);
            int y = rand.nextInt(GRID_SIZE);
            while (grid[x][y] != CRYSTAL) {
                grid[x][y] = PARTICLE;
                int direction = rand.nextInt(4);
                grid[x][y] = EMPTY;
                if (direction == 0) {
                    x = (x + 1) % GRID_SIZE;
                } else if (direction == 1) {
                    x = (x - 1 + GRID_SIZE) % GRID_SIZE;
                } else if (direction == 2) {
                    y = (y + 1) % GRID_SIZE;
                } else {
                    y = (y - 1 + GRID_SIZE) % GRID_SIZE;
                }
                if (isNextToCrystal(grid, x, y)) {
                    grid[x][y] = CRYSTAL;
                    break;
                }
            }
        }
    }

    public static boolean isNextToCrystal(int[][] grid, int x, int y) {
        return grid[(x + 1) % GRID_SIZE][y] == CRYSTAL ||
               grid[(x - 1 + GRID_SIZE) % GRID_SIZE][y] == CRYSTAL ||
               grid[x][(y + 1) % GRID_SIZE] == CRYSTAL ||
               grid[x][(y - 1 + GRID_SIZE) % GRID_SIZE] == CRYSTAL;
    }

    public static void printGrid(int[][] grid) {
        for (int i = 0; i < GRID_SIZE; i++) {
            for (int j = 0; j < GRID_SIZE; j++) {
                if (grid[i][j] == CRYSTAL) {
                    System.out.print("#");
                } else if (grid[i][j] == PARTICLE) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] grid = new int[GRID_SIZE][GRID_SIZE];
        simulateCrystalGrowth(grid);
        printGrid(grid);
    }
}