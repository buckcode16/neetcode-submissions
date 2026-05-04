class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sortS1 = sorted(s1)

        for i in range(len(s2)):
            lenS1 = len(sortS1)

            subStringS2 = sorted(s2[i:i+lenS1])

            if sortS1 == subStringS2:
                return True

        return False
