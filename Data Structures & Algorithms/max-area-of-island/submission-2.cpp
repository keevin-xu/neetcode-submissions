class Solution {
    using coord = std::tuple<int, int>;

public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();

        int out = 0;
        for (int i = 0; i < ROWS; ++i) {
            for (int j = 0; j < COLS; ++j) {
                if (grid[i][j] == 1) {
                    out = std::max(out, dfs(grid,i,j));
                }
            }
        }
        return out;
    }

private:
    int dfs(vector<vector<int>>& grid, int i, int j) {
        int ret = 0;
        std::stack<coord> stk;
        stk.push({i,j});

        int dR[4] = {-1,1,0,0};
        int dC[4] = {0,0,-1,1};

        while (!stk.empty()) {
            coord curr = stk.top();
            stk.pop();
            int r = std::get<0>(curr);
            int c = std::get<1>(curr);

            // with this approach that uses the grid as the "seen" collection,
            // must be careful because you might add the same location multiple times into the stack.
            if (grid[r][c] == 1) {
                ret++;
            }
            grid[r][c] = 0;
            for (int i = 0; i < 4; ++i) {
                int nR = r + dR[i];
                int nC = c + dC[i];
                if (nR >= 0 and nR < grid.size() and nC >= 0 and nC < grid[0].size() and grid[nR][nC] == 1) {
                    stk.push({nR,nC});
                }
            }
        }
        return ret;
    }
};
