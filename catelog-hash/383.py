from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        for char, size in r.items():
            if m.get(char, 0) < size:
                return False
        return True
