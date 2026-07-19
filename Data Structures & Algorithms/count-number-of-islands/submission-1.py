class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions =[[0, -1], #left
                             [0, 1],   #right
                             [-1, 0],   #up
                             [1, 0]]   #down
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands+=1
        return islands
