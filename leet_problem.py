from typing import List

class Solution:
    def LongestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0] #flower

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix


solution = Solution()
result = solution.LongestCommonPrefix(["flower", "flow", "flight"])
print("Longest common prefix:", result)
