class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # a = str(num)
        # res = 0
        # for i in a:
        #     res += int(i)
        # while res > 9:
        #     b = str(res)
        #     res = 0
        #     for j in b:
        #         res += int(j)
        # return res

        while len(str(num))>1:
            num = str(sum(map(int,str(num))))
        return int(num)