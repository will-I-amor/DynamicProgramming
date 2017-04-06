#从matrix左上角开始走，往最后一个右下角走，总共有几种走法
#https://www.youtube.com/watch?v=GO5QHC_BmvM&t=112s
G = [[''for i in range(m)]for i in range(n)]
for row in range(n):
    for col in range(m):
        if (row==0 or col==0):
            G[row][col]=1
        else:
            G[row][col] = G[row-1][col] +G[row][col-1]
