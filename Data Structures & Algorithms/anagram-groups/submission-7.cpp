class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::map<std::array<int, 26>, std::vector<std::string>> m;
        std::vector<std::vector<string>> out;
        for (const auto& str : strs) {
            std::array<int, 26> letters{};
            for (const auto& c : str) {
                letters[c - 'a'] += 1;
            }
            m[letters].push_back(str);
        }

        for (const auto& [key, value] : m) {
            out.push_back(value);
        }
        return out;
    }
};
