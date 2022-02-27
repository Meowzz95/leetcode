from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        min_len = len(min(strs, key=len))
        for i in range(0, min_len):
            comp = strs[0][i]
            success = True
            for s in strs:
                c = s[i]
                if c != comp:
                    success = False
                    break
            if success:
                i += 1
            else:
                break
        return strs[0][:i]
if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))



