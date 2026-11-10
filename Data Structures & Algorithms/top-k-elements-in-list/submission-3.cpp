class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::vector<int> out;
        std::unordered_map<int, int> m;
        for (const auto& n : nums) {
            m[n] = m[n] + 1;
        }
        std::priority_queue<std::pair<int,int>> pq;
        for (auto& [o,v] : m) {
            pq.push(std::pair<int,int>{v,o});
        }
        for (size_t i{}; i < k; ++i) {
            auto c = pq.top();
            pq.pop();
            out.push_back(c.second);
        }
        return out;
    }
};
