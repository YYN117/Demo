class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        key1 = 'qwertyuiop'
        key2 = 'asdfghjkl'
        key3 = 'zxcvbnm'
        ans = []
        for word in words:
            a = set(word.lower())
            if a.issubset(key1) or a.issubset(key2) or a.issubset(key3):
                ans.append(word)

        return ans

s1 = Solution()
a=["Hello","Alaska","Dad","Peace"]
print(s1.findWords(a))