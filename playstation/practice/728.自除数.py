class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left,right+1):
            ss = str(i)
            for j in ss:
                int_j = int(j)
                if int_j == 0:
                    break
                if i % int_j != 0:
                    break
                    
            else:
                res.append(i)
        return res


s1 = Solution()
print(s1.selfDividingNumbers(1, 22))