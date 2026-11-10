/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> out{};
    vector<vector<int>> levelOrder(TreeNode* root) {
        rec(root, 0);
        return out;
    }

    void rec(TreeNode* root, int level) {
        if (root == nullptr) {
            return;
        }
        if (level >= out.size()) {
            out.push_back(std::vector<int>{});
        }
        out[level].push_back(root->val);
        rec(root->left, level+1);
        rec(root->right, level+1);
    }
};
