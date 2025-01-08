class Solution {
    private int[][] sq;
    private int N;
    private int M;
    private int maxAreaGlobal = 0;

    private int maxSq(int row, int col, char[][] matrix) {        
        int maxChildSqRight = col < (M - 1) 
            ? (sq[row][col + 1] != -1 ? sq[row][col + 1] : maxSq(row, col + 1, matrix))
            : 0;
        int maxChildSqDown = row < (N - 1) 
            ? (sq[row + 1][col] != -1 ? sq[row + 1][col] : maxSq(row + 1, col, matrix))
            : 0;
        int maxChildSqRightDown = row < (N - 1) && col < (M - 1) 
            ? (sq[row + 1][col + 1] != -1 ? sq[row + 1][col + 1] : maxSq(row + 1, col + 1, matrix))
            : 0;

        if (sq[row][col] == -1) {
            sq[row][col] = ((matrix[row][col] == '1') ? 1 : 0) * (1 + Math.min(Math.min(maxChildSqRight, maxChildSqDown), maxChildSqRightDown));
        }
        maxAreaGlobal = Math.max(maxAreaGlobal, sq[row][col] * sq[row][col]);
        return sq[row][col];
    }
    public int maximalSquare(char[][] matrix) {
        sq = new int[matrix.length][matrix[0].length];
        N = matrix.length;
        M = matrix[0].length;
        for (int[] row : sq) {
            Arrays.fill(row, -1);
        }
        maxSq(0, 0, matrix);
        for (int[] row: sq) {
            for(int entry : row) {
                System.out.print(Integer.toString(entry) + " ");
            }
            System.out.print("\n");
        }
        return maxAreaGlobal;
    }
}