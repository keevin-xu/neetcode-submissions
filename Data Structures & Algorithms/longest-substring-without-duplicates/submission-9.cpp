class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int r = 0;
        std::unordered_set<char> charset;
        int max = 0;
        while (r < s.size()) {
            if (charset.contains(s[r])) {
                charset.erase(s[l]);
                l++;
            } else {
                charset.insert(s[r]);
                r++;
            }
            max = std::max(max, r-l);
        }
        return max;
    }
};
