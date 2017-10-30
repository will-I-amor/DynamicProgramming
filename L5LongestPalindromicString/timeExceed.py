class Solution(object):
    def longestPalindrome(self, mystr):
        """
        :type s: str
        :rtype: str
        """
        n = len(mystr)
        if (n==0 or n==1):return mystr
        G = [[0 for ii in range(n)] for jj in range(n)]
        mInt = 1
        reStr = ""
        for j in range(n):
            for i in range(n-j):#G[i][i+j]就是沿着斜线(对角线)开始算。比如先是[0][0],[1][1]...[5][5]
            #然后是[0][1],[1][2],[2][3],[3][4],[4][5]
                if (mystr[i]==mystr[i+j]):
                    if(j>=2):
                        if(G[i+1][i+j-1])==1:
                            G[i][i+j]=1
                            if j>=mInt:
                                mInt = j
                                reStr = mystr[i:i+j+1]
                        else:
                            G[i][i+j]=0
                    elif i==i+j:
                        G[i][i+j]=1
                        if j>=mInt:
                            mInt = j
                            reStr = mystr[i:i+j+1]
                    else:
                        G[i][i+j]=1
                        if j>=mInt:
                            mInt = j
                            reStr = mystr[i:i+j+1]
                else:
                    G[i][i+j]=0
        if reStr=="":
            return mystr[0]
        return reStr
