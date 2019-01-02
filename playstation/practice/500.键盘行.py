class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        keyset = ['qwertyuiop','asdfghjkl','zxcvbnm']
        for word in words:
            a = set(word.lower())
            for key in keyset:
                # for i in a:
                    # if i not in key:
                    #     break
                    # elif i == a[-1]:
                    #     ans.append(word)
                if a.issubset(set(key)):
                    ans.append(word)
        return ans
        '''
        res = []
        ref = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
               ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
               ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
        for i in words:
            ss = "".join(set(i.lower()))  # 要处理大小写问题
            for j in ref:
                for k in ss:
                    if k not in j:
                        break
                    elif k == ss[-1]:
                        res.append(i)
                        print(ss[-1])
        return res
'''


s1 = Solution()
a=["Hello","Alaska","Dad","Peace"]
print(s1.findWords(a))