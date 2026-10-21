class Solution {
public:
    int ROWS, COLS;
    bool exist(vector<vector<char>>& board, string word) {
        ROWS = board.size();
        COLS = board[0].size();
        for (int r = 0; r < ROWS; ++r) {
            for (int c = 0; c < COLS; ++c) {
                if (back(board, word, r, c, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

private:
    bool back(vector<vector<char>>& board, string word, int i, int j, int ind) {
        if (ind == word.size()) {
            return true;
        }

        if (i < 0 || i >= ROWS || j < 0 || j >= COLS || board[i][j] != word[ind] || board[i][j] == '#') {
            return false;
        }
        board[i][j] = '#';
        bool res = back(board, word, i+1, j, ind+1) || back(board, word, i-1, j, ind+1) || back(board, word, i, j+1, ind+1) || back(board, word, i, j-1, ind+1);
        board[i][j] = word[ind];
        return res;
    }
};
