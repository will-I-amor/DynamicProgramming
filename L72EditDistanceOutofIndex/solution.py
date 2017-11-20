class Solution(object):
    def minDistance(self, str1, str2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1 = len(str1)
        n2 = len(str2)
        if n1==0:
            return n2
        if n2==0:
            return n1
        G = [[0 for ii in range(n1+1)] for jj in range(n2+1)]
        for i in range(n2+1):#注意这里是i从0到n2+1,是n2而非n1.否则溢出
            for j in range(n1+1):
                if i==0 and j==0:
                    G[i][j] = 0
                elif i==0 and j!=0:#第一行填0，1，2，3...
                    G[i][j] = G[i][j-1]+1
                elif j==0 and i!=0:#第一列填0,1,2,3...
                    G[i][j] = G[i-1][j]+1
                else:
                    #注意这里str1[j-1],j对应str1。如果写反，溢出
                    if str1[j-1]==str2[i-1]:#如果当前字母相同，直接从斜上角copy，不用+1
                        G[i][j] = G[i-1][j-1]
                    else:#如果当前字母不同，取上，左，斜上角的3个格子中最小的数字，然后+1
                        G[i][j] = 1+min(G[i][j-1],G[i-1][j],G[i-1][j-1])
        return G[len(str2)][len(str1)]
