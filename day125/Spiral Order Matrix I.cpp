//pseudo
    //print left to right
    //move pointer of top lower
    //print top to bottom
    //move right pointer leftwards
    //print right to left
    //move bottom pointer upwards
    //print bottom to top
    //move left pointer rightwards
    //repeat
vector<int> Solution::spiralOrder(const vector<vector<int>>& v) {
    int rows = v.size();
    int cols = v[0].size();
    int left = 0, top = 0, right = cols - 1, bottom = rows - 1, total = 0;
    vector<int> result;
    while (total < rows * cols) {

        for (int j = left; j <= right && total < rows * cols; j++) {
            result.push_back(v[top][j]);
            total++;
        }
        top++; // move pointer of top lower

        for (int i = top; i <= bottom && total < rows * cols; i++) {
            result.push_back(v[i][right]);
            total++;
        }
        right--; // move right pointer leftwards

        for (int j = right; j >= left && total < rows * cols; j--) {
            result.push_back(v[bottom][j]);
            total++;
        }
        bottom--; // move bottom pointer upwards

        for (int i = bottom; i >= top && total < rows * cols; i--) {
            result.push_back(v[i][left]);
            total++;
        }
        left++; // move left pointer rightwards
    }
    return result;
}
