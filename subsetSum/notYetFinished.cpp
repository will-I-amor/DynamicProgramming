//given set[]= {3,34,4,12,5,2}
//find set that can sum up to 9, sum = 9
//return True, since {4,5} can sum up to 9
//http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/
bool subset[sum+1][n+1]
for (i=0;i<=n;i++)
{
  subset[0][i]=True
}
for (i=1;i<=sum;i++)
{
  subset[i][0] = False
}
for (i=1;i<=sum;i++)
{
  for (j=1;j<=n;j++)
  {
    subset[i][j] = subset[i][j-1]
    if (i>=set[j-1])
    {
      subset[i][j] = subset[i][j] || subset[i-set[j-1]][j-1]
      //难点在这里，上面这行
     }
   }
}
return sum[sum][n]
