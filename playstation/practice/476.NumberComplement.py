class Solution:
    def findComplement(self,num):
        #bin()输出为二进制  bin(5)='0b101'
        bin_num = bin(num)[2:]
        # bin_res = map(lambda x:'0' if x=='1' else 1 , bin_num)
        # return int(''.join(bin_res), 2)
        bin_res = ''
        for x in bin_num:
            if x == '1':
                bin_res += '0'
            else:
                bin_res += '1'
        res = int(bin_res,2)
        return res
