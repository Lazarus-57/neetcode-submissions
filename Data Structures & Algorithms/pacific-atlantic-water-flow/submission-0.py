class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        #to make rows and cols iterable
        rows, cols = len(heights), len(heights[0])

        #use two sets
        pacific_set = set()    #set 1 - the cells that can reach the pacific ocean
        atlantic_set = set()   #set 2 - the cells that can reach the atlantic ocean
        
        #directions
        directions = [[-1,0], #up
                      [1,0],  #down
                      [0,-1], #left
                      [0,1]]  #right

        def dfs(r, c, visited, prev_height):
            # First check - out of bounds?
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            # Second check - if the cell has already been visited or is too short
            if (r,c) in visited or heights[r][c] < prev_height:
                return
            # Add visited cell
            visited.add((r,c))
            # Check whether the water can flow up, down, left or right
            for dr, dc in directions:
                dfs(r+dr, c+dc, visited, heights[r][c]) #r+dr and c+dc are the directions heading up, down, left or right
        
        #Begin the exploration
        #Sweep the top and bottom rows
        for c in range(cols):
            dfs(0, c, pacific_set, heights[0][c])       #Pacific side
            dfs(rows-1, c, atlantic_set, heights[rows-1][c]) #Atlantic side
        
        #Sweep the left and right columns
        for r in range(rows):
            dfs(r, 0, pacific_set, heights[r][0])       #Pacific side
            dfs(r, cols-1, atlantic_set, heights[r][cols-1]) #Atlantic side
        
        #finally, find the common cells in each set and return them
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific_set and (r,c) in atlantic_set:
                    result.append((r,c))
        return result


