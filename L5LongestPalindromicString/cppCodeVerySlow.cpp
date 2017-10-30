//注意事项是31行的string.substr()这个function
//substr()接受2个变量(i,j),i是从第i位开始取，但是j是总共取多长，而不是到j位截止。这是c++跟python的区别
class Solution {
public:
    string longestPalindrome(string mystr) {
        if (mystr.length()==0 || mystr.length()==1) return mystr;
        int n = mystr.length();
        int G[n][n];
        int bInt = 1;
        string reStr = "";
        for (int ii=0;ii<n;ii++)
        {
            for (int jj=0;jj<n;jj++)
            {
                G[ii][jj]=0;
            }
        }
        for(int j=0;j<n;j++)
        {
            for (int i=0;i<n-j;i++)
            {
                if(mystr[i]==mystr[i+j])
                {
                    if(j>=2)
                    {
                        if(G[i+1][i+j-1]==1)
                        {
                            G[i][i+j]=1;
                            if (j>=bInt)
                            {
                                bInt = j;
                                reStr = mystr.substr(i,j+1);
                            }
                        }
                        else
                        {
                            G[i][i+j]=0;
                        }
                    }
                    else if (i==i+j)
                    {
                        G[i][i+j]=1;
                        if (j>=bInt)
                            {
                                bInt = j;
                                reStr = mystr.substr(i,j+1);
                            }
                    }
                    else
                    {
                        G[i][i+j]=1;
                        if (j>=bInt)
                            {
                                bInt = j;
                                reStr = mystr.substr(i,j+1);
                            }
                    }
                }
                else
                {
                    G[i][i+j]=0;
                }
            }
        }
        if (reStr=="")
        {
            reStr += mystr[0];
            return reStr;
        }
        return reStr;
        }
};
