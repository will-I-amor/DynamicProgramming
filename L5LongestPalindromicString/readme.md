    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example:

    Input: "babad"

    Output: "bab"

    Note: "aba" is also a valid answer.
    Example:

    Input: "cbbd"

    Output: "bb"
    

###### 斜着算，按对角线来算；如果两个字母相同，还要看他左斜方的cell是不是T；为什么是左斜下方？

###### 因为DP要看前一步的状态，左斜下方正好是前一步的状态

![](https://i.imgur.com/9mp7gKX.jpg)
![](https://i.imgur.com/X4wNgUY.jpg)
