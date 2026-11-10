class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> m;
        for (size_t i{}; i < nums.size(); i++) {
            m[nums[i]] = i;
        }
        for (size_t i{}; i < nums.size(); i++) {
            if (m.contains(target - nums[i]) && m[target - nums[i]] != i) {
                return std::vector<int>{static_cast<int>(i), m[target - nums[i]]};
            }
        }
    }
};
