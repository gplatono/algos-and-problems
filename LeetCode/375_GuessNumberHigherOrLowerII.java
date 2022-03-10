class Solution {
    private int[][] sums;
    
    public int dp(int i, int j) {
        if (i >= j)
            return 0;
        
        if (sums[i][j] == -1) {
           int mnum = 1000000000;
            for (int k = i; k <= j; k++) {
                int l = dp(i, k-1);
                int r = dp(k+1, j);
                mnum = Integer.min(mnum, (k+1) + Integer.max(l, r));
                //System.out.println(i + " " + j + " " + " " + k + " " + l + " " + r + " " + mnum);
            }
            sums[i][j] = mnum;
        }
        //System.out.println(i + " " + j + " " + sums[i][j]);
        return sums[i][j];
    }
    
    public int getMoneyAmount(int n) {
        sums = new int[n][n];
        for (int i=0; i<n; i++)
            for (int j = 0; j < n; j++) {
                if (i == j)
                    sums[i][i] = 0;
                else
                    sums[i][j] = -1;
                if (i < n-1)
                    sums[i][i+1] = i+1;
                if (i < n-2)
                    sums[i][i+2] = i+2;
            }
        return this.dp(0, n-1);        
    }
}