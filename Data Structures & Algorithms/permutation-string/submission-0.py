from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        count2 = Counter()

        l = 0
        k = len(s1)

        for r in range(len(s2)):

            count2[s2[r]] = count2.get(s2[r], 0) + 1

            if r - l + 1 > k:
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1

            if count1 == count2:
                return True

        return False