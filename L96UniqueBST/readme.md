    Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

    For example,
    Given n = 3, there are a total of 5 unique BST's.

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3

不论这3、4个数是什么，他们肯定是distinct的，而且肯定会有a>b>c。不论是1、2、3还是4、5、5。他们组成的BST的个数都是一样的

比如1、2、3、4这四个数。1为root，剩下3个数肯定全在1的右面(因为是BST，肯定在右面)；

2为root，{1}在左面，{3,4}在右面。那么就可以根据这个规律来用DP解题。

![](https://i.imgur.com/3qx325x.jpg)
