//想用表格法，对角线这样来算，但是超时了，不知道更efficient的方法是什么
int maxProfit(vector<int>& prices)
{
	int n = prices.size();
	vector<vector<int>>f(n,vector<int>(n,0));
	int maxI = 0;
  //算对角线，斜着算
	for (int j = 0;j<n;j++)
	{
		for(int i=0;i<n-j;i++)
		{
			f[i][i+j] = prices[i+j]-prices[i];
			if(f[i][i+j]>maxI)
			{
				maxI = f[i][i+j];
			}
		}
	}
	return maxI;
}
