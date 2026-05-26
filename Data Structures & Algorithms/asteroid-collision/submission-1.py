class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:

            while stack and stack[-1] > 0 and a < 0:
                diff = stack[-1] + a

                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                    break
                else:
                    a = 0
                    stack.pop()
                    break

            if a != 0:
                stack.append(a)

        return stack