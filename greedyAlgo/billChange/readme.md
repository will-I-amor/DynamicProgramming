#### bug出在第10行

     if i<=goal
 
 一定要有小于等于号
 
 否则死循环
 
 因为goal会不断减小，最后的值may等于goal
