class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        bool x = false;
        bool y = false;
        bool z = false;
        for (int i = 0; i < triplets.size(); ++i) {
            x = x || triplets[i][0] == target[0] && triplets[i][1] <= target[1] && triplets[i][2] <= target[2];
            y = y || triplets[i][0] <= target[0] && triplets[i][1] == target[1] && triplets[i][2] <= target[2];
            z = z || triplets[i][0] <= target[0] && triplets[i][1] <= target[1] && triplets[i][2] == target[2];
            if (x && y && z) {
                return true;
            }
        }
        return false;
    }
};
