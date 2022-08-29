class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        
        # Check if current square is a 1
        # Use depth first search to look at neighbouring areas for "1"s.
        
        #Case 1
        #["1","1","1","1","0"]  
        #["1","1","0","1","0"]
        #["1","1","0","0","0"]
        #["0","0","0","0","0"]
        
        #["0","1","1","1","0"]
        #["1","1","0","1","0"]
        #["1","1","0","0","0"]
        #["0","0","0","0","0"]
        
        #["0","0","0","0","0"]
        #["0","0","0","0","0"]
        #["0","1","0","0","0"]
        #["0","0","0","0","0"]
        
        def dfs(x, y):
            
            # if current square is a 0 or will go outside boundaries, exit search
            if (x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y]=="0"):
                return
            
            #turn current square into 0
            grid[x][y]="0"
            
            # search right square
            dfs(x,y+1)
            
            # search left square
            dfs(x,y-1)
            
            # search north square
            dfs(x+1,y)
            
            # search south square
            dfs(x-1,y)
            
            return
            
        for x in range(len(grid)):
            
            for y in range(len(grid[x])):
                
                if (grid[x][y] == "1"):
                    
                    dfs(x,y)
                    
                    islands+=1
        
        return islands
