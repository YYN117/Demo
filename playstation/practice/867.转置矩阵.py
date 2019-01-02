class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0:
            return []
        rows,cols = len(A),len(A[0])
        #len(A)是矩阵的行数，len(A[0])是矩阵的列数
        res = [[0]*rows for _ in range(cols)] #构建一个元素为0的矩阵
        '''
        _在python中称作 丢弃变量

如果不关心一个变量，就可以定义改变量的名字为_ 这是一个惯例，是一个不成文的约定，但不是标准

_是一个合法的标识符，也可以作为一个有效的变量使用，但是定义成下划线就是希望不要被使用，除非明确的知道这个数据需要使用
        '''

        for row in range(rows):
            for col in range(cols):
                res[col][row] = A[row][col]
        return res

if __name__ == '__mian__':
    solu = Solution()
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solu.transpose(A))


'''
问题分析：
这问题让我想到了48题，应该非常简单，或者说都没必要在这里写，我主要的目的是总结一下Python中的 zip 的用法哈。

Python3实现：
# @Time   :2018/7/9
# @Author :LiuYinxing
 
 
class Solution:
    def transpose(self, A):  # 方法一
        A[::] = zip(*A)
        return A
    
    def transpose1(self, A):  # 方法二
        if len(A) == 0: return []
        r, c = len(A), len(A[0])
        return [[A[i][j] for i in range(r)] for j in range(c)]
 
 
if __name__ == '__main__':
    solu = Solution()
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solu.transpose(A))
Python zip 总结：
（1）zip(): 相当于压缩，简单理解就是，把长度相等的几列数据，压缩成一个矩阵，变成按行储存。例如：

x = ['1', '2', '3']
y = ['a', 'b', 'c']
z = list(zip(x, y))
print(z)  # [('1', 'a'), ('2', 'b'), ('3', 'c')]
（2）zip(*):相当于解压，简单理解就是，把一个矩阵本来是一行一行的储存的，现在解压成一列一列的储存，相当于矩阵转置。例如：

x = [['1', 'a'], ['2', 'b'], ['3', 'c']]
z = list(zip(*x))
print(z)  # [('1', '2', '3'), ('a', 'b', 'c')]
注意：如果要直接输出，zip()内容要经过 list() 之后才能显示出来。
'''