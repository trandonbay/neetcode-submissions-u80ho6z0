class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first, second = Counter(s), Counter(t)

        if first == second:
            return True
        else:
            return False