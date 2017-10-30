#用2行list来存计算后的结果就够了。G[1]为存新算的，G[0]存上一次算完的。这样空间复杂度低一些
def minim(triangle):
    n = len(triangle)
    G = [[1000000 for ii in range(n)] for jj in range(2)]
    for i in range(2):
        for j in range(i+1):
            G[1][j] = triangle[i][j]
            if(i==0 and j==0):
                continue
            if (j==0):
                G[1][j]+=G[0][j]
            elif (j==i):
                G[1][j]+=G[0][j-1]
            else:
                G[1][j]+=min(G[0][j-1],G[0][j])
        G[0],G[1]=G[1],G[0]
    a = min(G[0])
    print(G)
    print (a)
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
minim(triangle)
