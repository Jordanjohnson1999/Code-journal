class solutions:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


solution = solutions()
print("Test 1 - Expected True:", solution.isAnagram("anagram", "nagaram"))
print("Test 2 - Expected False:", solution.isAnagram("rat", "car"))
print("Test 3 - Expected True:", solution.isAnagram("listen", "silent"))
print("Test 4 - Expected False:", solution.isAnagram("hello", "helloo"))
