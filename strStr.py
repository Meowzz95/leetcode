class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        lps = self.compute_lps(needle)
        return self.kmp_search(haystack,needle,lps)

    def kmp_search(self, haystack:str, needle:str, lps:list[int]):
        lh=len(haystack)
        ln=len(needle)
        i=0
        j=0
        while i<lh:
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            if j==ln:
                # print(f"found at index {i-j}")
                return i-j
                j=lps[j-1]
            elif i<lh and haystack[i]!=needle[j]:
                if j!=0:
                    j = lps[j-1]
                else:
                    i+=1
        return -1


    def compute_lps(self,needle:str):
        ln = len(needle)
        lps=[0]*ln
        i = 1
        last_longest_len=0
        while i<ln:
            if needle[i]==needle[last_longest_len]:
                last_longest_len+=1
                lps[i]=last_longest_len
                i+=1
            else:
                if last_longest_len!=0:
                    last_longest_len = lps[last_longest_len-1]
                else:
                    lps[i]=0
                    i+=1
        return lps



print(Solution().compute_lps("AAACAAAA"))
print(Solution().strStr("hello", "ll"))