#设置了障碍，有障碍的格子是数字1表示的
#此code单算了第一行，和第一列
#只打败4%的人，有够慢的，需要优化
def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid[0])#col
        n = len(obstacleGrid)#row
        if obstacleGrid[0][0]==1:
            return 0
        else:
            obstacleGrid[0][0]=1#设成1，不然后面没法写。把[0][0]拿出来单算。。
            for i in range(1,m):#第一行
                if obstacleGrid[0][i]==1:
                    obstacleGrid[0][i]=0
                else:
                    obstacleGrid[0][i]=obstacleGrid[0][i-1]
            for j in range(1,n):#第一列
                if obstacleGrid[j][0]==1:
                    obstacleGrid[j][0]=0
                else:
                    obstacleGrid[j][0]=obstacleGrid[j-1][0]
            for row in range(1,n):
                for col in range(1,m):
                    if obstacleGrid[row][col]==1:
                        obstacleGrid[row][col]=0
                    else:
                        obstacleGrid[row][col]= obstacleGrid[row-1][col]+obstacleGrid[row][col-1]
            return obstacleGrid[n-1][m-1]
