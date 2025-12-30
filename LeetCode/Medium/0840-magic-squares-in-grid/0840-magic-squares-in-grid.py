def griidd(grid,row,col):
    d={}
    for i in range(3):
        for j in range(3):
            if grid[row+i][col+j]<1 or grid[row+i][col+j]>9 or grid[row+i][col+j] in d:
                return False
            d[grid[row+i][col+j]]=1
    col1=grid[row][col]+grid[row+1][col]+grid[row+2][col]
    col2=grid[row][col+1]+grid[row+1][col+1]+grid[row+2][col+1]
    col3=grid[row][col+2]+grid[row+1][col+2]+grid[row+2][col+2]
    if(col1!=col2 or col2!=col3 or col1!=col3):
        return False
    row1=grid[row][col]+grid[row][col+1]+grid[row][col+2]
    row2=grid[row+1][col]+grid[row+1][col+1]+grid[row+1][col+2]
    row3=grid[row+2][col]+grid[row+2][col+1]+grid[row+2][col+2]
    if(row1!=row2 or row2!=row3 or row1!=row3):
        return False
    if row1!=col1:
        return False
    dia1=grid[row][col]+grid[row+1][col+1]+grid[row+2][col+2]
    dia2=grid[row+2][col]+grid[row+1][col+1]+grid[row][col+2]
    if dia1!=dia2:
        return False
    if dia1!=col1:
        return False
    return True
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans=0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if griidd(grid,i,j):
                    ans+=1
        return ans