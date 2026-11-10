class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int low = 0;
        int high = matrix.size() * matrix[0].size() - 1;

        int ROWS = matrix.size();
        int COLS = matrix[0].size();
        //row * COLS + col
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int r = mid / COLS;
            int c = mid % COLS;
            if (matrix[r][c] == target) {
                return true;
            } else if (matrix[r][c] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return false;
    }
};
