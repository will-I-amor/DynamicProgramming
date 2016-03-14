#include <iostream>
#include <limits.h>
using namespace std;
int cut2(int price[],int n, int rem[]);
int max(int a, int b)
{
	return (a>b)?a:b;
}
int cut1(int price[],int n)
{
	int rem[n];
	for(int i = 0;i<=n;i++)
	{
		rem[i] = INT_MIN;
	}
	return cut2(price,n,rem);
}
int cut2(int price[],int n, int rem[])
{
	int q = INT_MIN;
	if(rem[n]>=0)
	{
		return rem[n];
	}
	if(n == 0)
	{
		q = 0;
	}
	else
	{
		q = INT_MIN;
		for(int i = 0;i<n;i++)
		{
			q = max(q,price[i]+cut2(price,n - i - 1,rem));
		}
	}
	rem[n] = q;
	return q;
}
int main()
{
	int arr[] = {1,5,8,9,10,17,17,20,24,30};
	int result = cut1(arr,9);
	cout<<result<<endl;
	return 0;
}
