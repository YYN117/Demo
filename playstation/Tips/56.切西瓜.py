'''
描述:
小Py要吃西瓜，想知道切了n刀后，最多能切出多少块？请你们帮助下小Py.
给你一个正整数n（0 < n < 10^3),你输出一个数字，代表最多能切多少块。
如n=1, 输出2。
'''
n = int(input('n:'))
print((n**3 + 5*n + 6)//6)

'''
我们先假设有n个平面相交得到了a(n)个空间，我们再添加第n+1个平面，第n+1个平面和其余的平面两辆相交，得到最大分割，也就是说第n+1个平面被分割成n条线分割，最大能分割成你b(n)=(n+1)*n/2+1个平面（为什么分割成这么多多平面见：这里）被分割成的子平面又把原来的空间一分为二，所以增加了b(n)个空间，可以得出a(n+1)=a(n)+b(n)<==>a(n+1)-a(n)=b(n);
a(2)-a(1)=b(1);
a(3)-a(2)=b(2);
    ....
a(n)-a(n-1)=b(n-1);
得出：
a(n)-a(1)=b(1)+b(2)+...+b(n-1);又a(1)=2;
a(n)=2+b(1)+b(2)+...+b(n-1);
经过变形：b(n)=1/2(n 2+n+2)
b(1)+...+b(n-1)=1/2[(12+22 .... +(n-1)2)+(1+2+..+n-1)+2(n-1)]
平方和公式：n(n+1)(2n+1)/6
最终得到：a(n)=(n3+5n+6)/6 
'''

