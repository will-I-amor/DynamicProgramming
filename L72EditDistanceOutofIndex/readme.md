    Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

    You have the following 3 operations permitted on a word:

    a) Insert a character
    b) Delete a character
    c) Replace a character
    
    这道题容易溢出，之前写了一种方法，但是如果str1 = 'a', str2 = 'ab',两个字符串长度不同，就会溢出。
    所以在i,j的选择上要注意
![](https://i.imgur.com/7MBViXi.jpg)

![](https://i.imgur.com/Zfx6FGp.jpg)
