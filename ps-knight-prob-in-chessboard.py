class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def move(n, r, c, k):
            if r < 0 or c < 0 or r >= n or c >= n or k < 0:
                return 0
            if k == 0:
                return 1
            return move(n, r-2, c+1, k-1) \
            +move(n, r-1, c+2, k-1) \
            +move(n, r+1, c+2, k-1) \
            +move(n, r+2, c+1, k-1) \
            +move(n, r+2, c-1, k-1) \
            +move(n, r+1, c-2, k-1) \
            +move(n, r-1, c-2, k-1) \
            +move(n, r-2, c-1, k-1)

        res = move(n, row, column, k)
        return res/pow(8, k)