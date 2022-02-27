class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        max_p_str = s[0]
        max_p_len = 1
        for i in range(0, len(s) - 1):
            # consecutive two like 'aa'
            if s[i] == s[i + 1]:
                c_max_str = self.max_palindrome(i, i + 2)
                if len(c_max_str) > max_p_len:
                    max_p_len = len(c_max_str)
                    max_p_str = c_max_str
            # min palindrome like 'aba'
            if i + 2 < len(s) and self.s[i] == self.s[i + 2]:
                c_max_str = self.max_palindrome(i, i + 3)
                if len(c_max_str) > max_p_len:
                    max_p_len = len(c_max_str)
                    max_p_str = c_max_str
        return max_p_str

    # start incl, end excl
    # eg: abcde
    #      bc   -> 1,3
    def max_palindrome(self, start, end):
        while True:
            # print('start',start,'end',end)
            if start - 1 < 0 or end > len(self.s) - 1:
                return self.s[start:end]
            if self.s[start - 1] == self.s[end]:
                start -= 1
                end += 1
            else:
                return self.s[start:end]

    def is_palindormic(self, s):
        # print(f'testing {s}')
        i = 0
        e = len(s) - 1
        while i < len(s) // 2:
            if s[i] != s[e]:
                return False
            i += 1
            e -= 1
        return True


print(Solution().longestPalindrome(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))