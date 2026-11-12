class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        std::priority_queue<int> pq;
        for (const auto& s : stones) {
            pq.push(s);
        }
        while (pq.size() > 1) {
            int first = pq.top();
            pq.pop();
            int second = pq.top();
            pq.pop();
            pq.push(std::max(first, second) - std::min(first, second));
        }
        if (pq.empty()) {
            return 0;
        }
        return pq.top();
    }
};
