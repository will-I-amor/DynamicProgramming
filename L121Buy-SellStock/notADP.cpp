class Solution {
public:
//遍历数组，设2个值，一个min，一个max. min值初始化成INT_MAX,如果初始化成INT_MIN，是会出错的，最后的结果也是错的
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int minI = INT_MAX;
        int maxI = 0;
        for (int i = 0;i<n;i++)
        {
            if(prices[i]<minI)
            {
                minI = prices[i];
            }
            else
            {
                maxI = max(maxI,prices[i]-minI);
            }
        }
        return maxI;
    }
};
