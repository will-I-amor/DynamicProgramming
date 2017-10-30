    Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

    For example, given the following triangle
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

    Note:
    Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
    
###### 状态转移方程：f[i][j]+=min(f[i-1][j],f[i-1][j-1])
###### 这道题难点主要是要想之前的元素，就是f[i][j]由上一层的元素加出来。而不是上一层的元素怎么加能加出下一层。
