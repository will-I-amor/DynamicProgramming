val = [1,4,5,7]
wt = [1,3,4,5]
G = [[''for i in range(8)]for i in range(4)]
for i in range(4):
    G[i][0]=0
for i in range(1,8):
    G[0][i]=1
for row in range(1,4):
    for col in range(8):
        if (col<wt[row]):
            G[row][col]=G[row-1][col]
        else:
            G[row][col]= max((val[row]+G[row-1][col-wt[row]]),(G[row-1][col]))
for i in G:
    print i
    
#the output is:               
#[0, 1, 1, 1, 1, 1, 1, 1]
#[0, 1, 1, 4, 5, 5, 5, 5]
#[0, 1, 1, 4, 5, 6, 6, 9]
#[0, 1, 1, 4, 5, 7, 8, 9]
#video:https://www.youtube.com/watch?v=8LusJS5-AGo
