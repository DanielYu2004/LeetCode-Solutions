class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lista = s.split()
        if lista == []:
            return 0
        else:
            return len(lista[-1])
