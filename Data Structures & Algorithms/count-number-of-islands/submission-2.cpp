class Solution {
public:
    int ROWS;
    int COLS;
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) { return 0;}
        int out = 0;
        ROWS = grid.size();
        COLS = grid[0].size();
        int max = grid.size() * grid[0].size();


        for (size_t i{}; i < max; i++) {
            if (grid[i / COLS][i % COLS] == '1') {
                bfs(grid, i);
                out++;
            }
        }
        return out;
    }
    void bfs(vector<vector<char>>& grid, int i) {
        std::queue<int> q;
        q.push(i);
        grid[i / COLS][i % COLS] = '0';
        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};

        while (!q.empty()) {
            int curr = q.front();
            q.pop();

            int r = curr / COLS;
            int c = curr % COLS;

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS) {
                    if (grid[nr][nc] == '1') {
                        grid[nr][nc] = '0'; 
                        q.push(nr * COLS + nc); 
                    }
                }
            }
        }
    }  
};
