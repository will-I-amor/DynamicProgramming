#[[2]               [[2]
# [3,4]              [5,6]
# [6,5,7]            [11,10,11]
# [4,1,8,3]]         [15,11,18,14]]
#状态转移方程：f[i][j]+=min(f[i-1][j],f[i-1][j-1])
#这道题难点主要是要想之前的元素，就是f[i][j]由上一层的元素加出来。而不是上一层的元素怎么加能加出下一层。

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        #以一个很大的数初始化数组，这样越界的时候能看出来
        #G这个数组，每行都是N，即triangle最长的那一行的个数，比如G第二行是[3,4,100000,100000]
        G = [[1000000 for ii in range(n)] for jj in range(n)]
        for i in range(n):
            for j in range(i+1):
                G[i][j] = triangle[i][j]
                if(i==0 and j==0):#如果是第一行，就continue不管他
                    continue
                if (j==0):#极端条件，当遍历到行的第1个元素时
                    G[i][j]+=G[i-1][j]
                elif (j==i):#极端条件，当遍历到行的最后1个元素时，只有1种方法能加出G[i][j]
                    G[i][j]+=G[i-1][j-1]
                else:
                    G[i][j]+=min(G[i-1][j-1],G[i-1][j])
        a = min(G[n-1])
        return a
