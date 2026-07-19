class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()  # track the current panth

        def dfs(r, c, i):
            # Base Case 1: Found the entire word
            if i == len(word):
                return True
            
            # Base Case 2: Out of bounds, wrong character, or already visited
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False
            
            # Step 1: Add current cell to path before exploring
            path.add((r, c))
            
            # Step 2: Explore all 4 adjacent directions
            res = (dfs(r + 1, c, i + 1) or  # Down
                   dfs(r - 1, c, i + 1) or  # Up
                   dfs(r, c + 1, i + 1) or  # Right
                   dfs(r, c - 1, i + 1))    # Left
            
            # backtrack
            path.remove((r, c))
            
            return res

        # Begin the DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
                    
        return False