class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        int prev2 = nums[0];
        nums[1] = std::max(nums[1], nums[0]);
        int prev1 = nums[1];
        for (size_t i = 2; i < nums.size(); i++) {
            nums[i] = std::max(prev1, prev2 + nums[i]);
            prev1 = nums[i];
            prev2 = nums[i-1];
        }
        return nums[nums.size()-1];
    }
};
