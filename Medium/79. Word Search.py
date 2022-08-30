class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        i, j = len(board), len(board[0])
        
        def get_neighbours(x,y):
            
            return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        
        def check_bounds(x, y):
            
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                
                return True
            
            else:
                
                return False
        
        def search (x, y, length):
            
            if (length == len(word)):
                
                return True
            
            for i in get_neighbours(x, y):
                
                look_x, look_y = i
                
                if (check_bounds(look_x, look_y) and (look_x, look_y) not in visited and board[look_x][look_y] == word[length]):
                    
                    visited.add((look_x, look_y))
                    
                    if (search(look_x, look_y, length+1)):
                        
                        return True
                    
                    visited.remove((look_x, look_y))
                    
            return False
        
        for x in range(i):
            
            for y in range(j):
                
                if (board[x][y] == word[0]):
                    
                    visited = set()
                    
                    visited.add((x, y))
                    
                    if (search(x, y, 1)):
                        
                        return True
                    
        return False
                    
                    #k = get_neighbours(x, y)
                    #for c in k:
                    #    if check_bounds(c[0],c[1]):
                    #        print(x, c, board[c[0]][c[1]])
