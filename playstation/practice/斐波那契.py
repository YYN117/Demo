class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0 or n == 1:
            return n
        p,q = 0,1
        for i in range(2,n+1):

            p,q = q,p+q
        return q
