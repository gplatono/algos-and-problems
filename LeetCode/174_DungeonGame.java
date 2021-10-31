class Solution {
    //Dimensions
    private static int m;
    private static int n;
    
    //min health required to complete from this position
    private static int[][] minHealth;    
    
    private static int[][] dungeon;
    private static final int INFTY = Integer.MAX_VALUE;
    
    private int findMinHealth(int i, int j) {
        if (minHealth[i][j] == INFTY) {
            int rHealth = INFTY, dHealth = INFTY;
                        
            //If not the bottom row, see the min health needed to go below
            if (i < m - 1)
                dHealth = Integer.max(1, findMinHealth(i + 1, j) - dungeon[i][j]);
            //If not the rightmost column, see the min health needed to go to the right
            if (j < n - 1)
                rHealth = Integer.max(1, findMinHealth(i, j+1) - dungeon[i][j]);
            
            minHealth[i][j] = Integer.min(dHealth, rHealth);
        }            
        return minHealth[i][j];
    }
    
    public int calculateMinimumHP(int[][] dungeon) {
        this.dungeon = dungeon;        
        m = dungeon.length;
        n = dungeon[0].length;
        minHealth = new int[m][];        
        for (int i = 0; i < m; i++) {
            minHealth[i] = new int[n];
            for (int j = 0; j < n; j++) 
                minHealth[i][j] = INFTY;
        }
        
        minHealth[m-1][n-1] = Integer.max(1, 1 - dungeon[m-1][n-1]);
        
        return findMinHealth(0, 0);
    }
}