#include <iostream>
#include <vector>
using namespace std;
int numTrees(int n)
{
	if(n==0){return 0;}
	else
	{
		vector<int>vec;
		vec.push_back(1);
		vec.push_back(1);
		for (int i = 2;i<=n;i++)
		{
			vec.push_back(0);
			for (int j=0;j<i;j++)
			{
				vec[i]+=vec[j]*vec[i-j-1];
			}
		}
		return vec[n];
	}
}
int main()
{
	int a = 0;
	a = numTrees(4);
	cout<<"a: "<<a<<endl;
	return 0;
}
