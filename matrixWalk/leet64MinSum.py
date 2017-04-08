#此题与之前几题很像，区别是求最小值。目标grid[row][col]怎样才能走到？2种途径，从grid[row-1][col]走，或从grid[row][col-1]走
def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])#col
        n = len(grid)#row
        for i in range(1,n):#first col
            grid[i][0]+=grid[i-1][0]
        for j in range(1,m):#first row
            grid[0][j]+=grid[0][j-1]
        for row in range(1,n):
            for col in range(1,m):
                grid[row][col]+=min(grid[row-1][col],grid[row][col-1])
        return grid[n-1][m-1]
