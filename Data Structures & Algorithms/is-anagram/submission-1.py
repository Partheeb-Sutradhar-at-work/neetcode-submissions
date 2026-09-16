class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        CountS = [0] * 26
        CountT = [0] * 26

        for z in s:
            CountS[ord(z) - ord('a')] += 1
        for z in t:
            CountT[ord(z) - ord('a')] += 1


        if CountT != CountS:
            return False
        return True 
        print(seen)
        