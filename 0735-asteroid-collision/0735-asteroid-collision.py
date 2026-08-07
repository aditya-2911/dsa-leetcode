class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
                continue

            flag = True
            size = -a
            
            while stack and a < 0 and stack[-1] > 0:
                top = stack[-1]
                if size > top:
                    stack.pop()
                elif size == top:
                    stack.pop()
                    flag = False
                    break
                else:
                    flag = False
                    break
            if flag:
                stack.append(a)

        return stack
