## 根据先序遍历和中序遍历重构二叉树
```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.size() != inorder.size()) {
            return NULL;
        }
        
        int n = preorder.size();
        return build(preorder, inorder, 0, n-1, 0, n-1);
    }
    
    TreeNode *build(vector<int> &pre, vector<int> &in, int pBegin, int pEnd, int iBegin, int iEnd) {
        if (pBegin > pEnd || iBegin > iEnd || pEnd - pBegin != iEnd - iBegin) {
            return NULL;
        }
        
        TreeNode *root = new TreeNode(pre[pBegin]);
        int inRootIndex = iBegin;
        for (int i = iBegin + 1; i <= iEnd; i++) {
            if (in[i] == root->val) {
                inRootIndex = i;
                break;
            }
        }
        if (in[inRootIndex] != root->val) {
            return NULL;
        }
        
        int leftLen = inRootIndex - iBegin;
        int iLeftBegin = iBegin, iLeftEnd = inRootIndex - 1;
        int iRightBegin = inRootIndex + 1, iRightEnd = iEnd;
        int pLeftBegin = pBegin + 1, pLeftEnd = pLeftBegin + leftLen-1;
        int pRightBegin = pLeftEnd + 1, pRightEnd = pEnd;
        
        root->left = build(pre, in, pLeftBegin, pLeftEnd, iLeftBegin, iLeftEnd);
        root->right = build(pre, in, pRightBegin, pRightEnd, iRightBegin, iRightEnd);
        
        return root;
    }
};
```