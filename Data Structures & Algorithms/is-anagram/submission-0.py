class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countt = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
        for char in t:
                     if char not in countt:
                         countt[char] = 1
                     else:
                         countt[char] += 1
        return countt == counts
solution = Solution()
result = solution.isAnagram(s='racecar', t='racaer')
print(result)
