//bfs from the treasures outward.

class Solution {
public:
    std::queue<std::tuple<int,int>> q;
    int INF = 2147483647;

    void islandsAndTreasure(vector<vector<int>>& grid) {
        q = std::queue<std::tuple<int,int>>();
        int ROWS = grid.size();
        int COLS = grid[0].size();
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (grid[i][j] == 0) {
                    //std::cout << i << ", " << j << "\n";
                    q.push({i,j});
                }
            }
        }
        bfs(grid, ROWS, COLS);
    }
private:
    int directionR[4] = {-1,1,0,0};
    int directionC[4] = {0,0,-1,1};

    void bfs(vector<vector<int>>& grid, int ROWS, int COLS) {
        while (!q.empty()) {
            std::tuple<int,int> curr = q.front();
            q.pop();
            int r = std::get<0>(curr);
            int c = std::get<1>(curr);
            for (int i = 0; i < 4; ++i) {
                int newR = r + directionR[i];
                int newC = c + directionC[i];
                if (newR >= 0 && newR < ROWS && newC >= 0 && newC < COLS && grid[newR][newC] == INF) {
                    grid[newR][newC] = grid[r][c] + 1;
                    q.push({newR,newC});
                }
            }
        }
    }
};