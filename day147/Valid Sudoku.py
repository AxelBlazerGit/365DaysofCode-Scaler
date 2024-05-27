class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        for i in range(9):
            rowTemp = set()
            colTemp = set()
            gridTemp = set()
            for j in range(9):
                if A[i][j] != "." and A[i][j] in rowTemp:
                    return 0
                rowTemp.add(A[i][j])
                if A[j][i] != "." and A[j][i] in colTemp:
                    return 0
                colTemp.add(A[j][i])
                rowStart, colStart = 3 * (i // 3), 3 * (i % 3)
                if A[rowStart + j // 3][colStart + j % 3] != "." and A[rowStart + j // 3][colStart + j % 3] in gridTemp:
                    return 0
                gridTemp.add(A[rowStart + j // 3][colStart + j % 3])
        return 1


# solution = Solution()

# sudoku_board = (
#     "53..7....",
#     "6..195...",
#     ".98....6.",
#     "8...6...3",
#     "4..8.3..1",
#     "7...2...6",
#     ".6..34128",
#     "...419..5",
#     "....8..79"
# )
# print(solution.isValidSudoku(sudoku_board))
