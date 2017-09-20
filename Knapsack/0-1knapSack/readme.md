最初级的背包问题，0/1knapSack是要么取这个item，要么leave it

    1. 建2个list，val[] (价值) 和 wt[] (重量)

    2. 把wt[] sort了，按照重量大小sort

    3. 建一个K[n+1][W+1]。有一行和一列都是0，所以+1

![](https://i.imgur.com/anjCXDS.jpg?1)

![](https://i.imgur.com/ESctmdc.jpg)
