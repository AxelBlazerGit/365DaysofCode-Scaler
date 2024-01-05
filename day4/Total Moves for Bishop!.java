
public class Solution {
    public int solve(int row, int col) {
        int diagonal1 = Math.min(row-1, col-1);
        int diagonal2 = Math.min(row-1, 8-col);
        int diagonal3 = Math.min(8-row, col-1);
        int diagonal4 = Math.min(8-row, 8-col);

    
        int total_squares = diagonal1 + diagonal2 + diagonal3 + diagonal4;

        return total_squares;
    }
}
