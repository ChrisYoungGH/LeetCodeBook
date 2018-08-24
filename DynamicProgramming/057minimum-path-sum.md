## 矩阵左上角到右下角的最小路径和
###解法
动态规划：
f(i,j) = min(f(i-1,j), f(i,j-1)) + a[i,j]
f(i,0) = f(i-1,0) + a[i,0]
f(0,j) = f(0,j-1) + a[0,j]
f(0,0) = a[0,0]
```c++
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        if (!m) {
            return 0;
        }
        int n = grid[0].size();
        if (!n) {
            return 0;
        }
        
        int dp[m][n] = {0};
        dp[0][0] = grid[0][0];
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        for (int j = 1; j < n; j++) {
            dp[0][j] = dp[0][j-1] + grid[0][j];
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        
        return dp[m-1][n-1];
    }
};
```