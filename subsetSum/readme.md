![](http://ww1.sinaimg.cn/large/0060lm7Tgy1fdxqpsitgzj30ow0j1mxz.jpg)  

    for (i=0;i<=n;i++)
    {
      subset[0][i] =  True
    }
    
    
上面的代码是给第一行，填上 True


    for (i=1;i<=sum;i++)
    {
      subset[i][0] = False
    }
    
    
这部分代码是给第1列填上False


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
      
      
      
subset[i][j] = subset[i][j] || subset[i-set[j-1]][j-1]

这个最不好理解。subset[i][j]已经被赋上他之前元素(subset[i][j-1])的值;这行是取True or False以后的值。就是只要有一个True就是True。

        subset[i-set[j-1]]
因为i是从[1到sum]，i-set[j-1]就是用sum减去当前set[j-1]的数，因为j多算一个，所以要j-1。比如当前sum是7,然后从set的第0个元素算起，即3.
       
       
i-set[j-1]就是4,j-1是0.取subset[4][0]，为False
       
有一种感觉就是他和她之前的元素，sum-item的差
           
      
