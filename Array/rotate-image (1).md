## 顺时针旋转二维数组90度
### 解法
- 对角线转置
- 上下翻转
- 对角线转置
- 反对角线转置
```c++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        if (!n) {
            return;
        }
        if (matrix[0].size() != n) {
            return;
        }
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        
        for (int i = 0; i < n / 2; i++) {
            for (int j = 0; j < n; j++) {
                swap(matrix[i][j], matrix[n-i-1][j]);
            }
        }
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
                swap(matrix[i][j], matrix[n-j-1][n-i-1]);
            }
        }
    }
};
```