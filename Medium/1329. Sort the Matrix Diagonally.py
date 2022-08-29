class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dummy = []
        y_bound, x_bound = len(mat)-1,len(mat[0])-1
        cur_x, cur_y = 0, 2
        while (cur_x <= x_bound):
            look_x, look_y = cur_x, cur_y
            temp_dummy = []
            temp_dummy.append(mat[cur_y][cur_x])
            while (look_y - 1 <= y_bound and look_y - 1 >= 0 and look_x - 1 >= 0):
                look_y, look_x = look_y-1,look_x-1
                temp_dummy.append(mat[look_y][look_x])
                
            temp_dummy.sort(reverse=True)
            
            look_x, look_y = cur_x, cur_y
            
            mat[cur_y][cur_x] = temp_dummy[0]
            
            index = 1
            
            while (look_y - 1 <= y_bound and look_y - 1 >= 0 and look_x - 1 >= 0):
                
                look_y, look_x = look_y-1,look_x-1
                
                mat[look_y][look_x] = temp_dummy[index]
                
                index += 1
                
            print(mat)
            cur_x += 1
            
        cur_x, cur_Y = 3, 0
        print(dummy)
            
